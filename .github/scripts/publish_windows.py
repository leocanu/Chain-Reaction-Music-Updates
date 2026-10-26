"""Reassemble only the verified installer; temporary upload branch is removed after publication."""
from pathlib import Path
import hashlib,json,os,re,subprocess
meta=json.loads(Path('windows-upload/manifest.json').read_text())
assert re.fullmatch(r'windows-v[0-9]+\.[0-9]+\.[0-9]+-rc[0-9]+',meta['tag'])
assert re.fullmatch(r'ChainReactionMusic-Setup-[0-9]+\.[0-9]+\.[0-9]+\.exe',meta['filename'])
assert re.fullmatch(r'[a-f0-9]{64}',meta['sha256'])
assert 0<meta['bytes']<2*1024**3 and 0<len(meta['parts'])<=30
out=Path('public-release');out.mkdir()
installer=out/meta['filename'];total=hashlib.sha256();size=0
with installer.open('wb') as target:
 for part in meta['parts']:
  assert re.fullmatch(r'part-[0-9]{3}\.bin',part['file'])
  digest=hashlib.sha256();count=0
  with (Path('windows-upload')/part['file']).open('rb') as source:
   while chunk:=source.read(1024*1024):target.write(chunk);total.update(chunk);digest.update(chunk);size+=len(chunk);count+=len(chunk)
  assert count==part['bytes'] and digest.hexdigest()==part['sha256'],'Upload part mismatch'
assert size==meta['bytes'] and total.hexdigest()==meta['sha256'],'Installer mismatch'
checksum=out/'SHA256SUMS.txt';checksum.write_text(meta['sha256']+'  '+meta['filename']+'\n')
notes=out/'release-notes.md';notes.write_text(meta['notes'])
def gh(*args,check=True,capture=False):
 return subprocess.run(['gh',*args],check=check,capture_output=capture,text=True)
lookup=gh('api','repos/'+os.environ['GH_REPO']+'/releases/tags/'+meta['tag'],check=False,capture=True)
if lookup.returncode==0:
 release=json.loads(lookup.stdout)
 if not release['draft']:
  existing=next((a for a in release['assets'] if a['name']==meta['filename']),None)
  assert existing and existing['size']==size and existing.get('digest')=='sha256:'+meta['sha256'],'Existing public release differs; refusing replacement'
  print(release['html_url']);raise SystemExit(0)
else:
 gh('release','create',meta['tag'],'--title',meta['title'],'--notes-file',str(notes),'--target',os.environ['DEFAULT_BRANCH'],'--draft','--prerelease')
gh('release','upload',meta['tag'],str(installer),str(checksum),'--clobber')
release=json.loads(gh('api','repos/'+os.environ['GH_REPO']+'/releases/tags/'+meta['tag'],capture=True).stdout)
asset=next(a for a in release['assets'] if a['name']==meta['filename'])
assert asset['size']==size and asset.get('digest')=='sha256:'+meta['sha256'],'Remote uploaded digest mismatch'
gh('release','edit',meta['tag'],'--draft=false','--prerelease','--latest=false')
url='https://github.com/'+os.environ['GH_REPO']+'/releases/tag/'+meta['tag']
with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as summary:summary.write('Windows candidate: '+url+'\n\nSHA256: '+meta['sha256']+'\n')
print(url)
