"""Build emaki.<ver>.nupkg without dotnet: OPC zip with nuspec, tools/, rels, content types, core properties."""
import re, sys, uuid, zipfile, pathlib
from xml.sax.saxutils import escape
spec = pathlib.Path("emaki.nuspec").read_text()
get = lambda t: re.search(rf"<{t}>(.*?)</{t}>", spec, re.S).group(1)
ver, ident = get("version"), get("id")
desc = re.search(r"<!\[CDATA\[(.*?)\]\]>", spec, re.S).group(1)
psm = uuid.uuid4().hex
out = pathlib.Path("out"); out.mkdir(exist_ok=True)
nupkg = out / f"{ident}.{ver}.nupkg"
with zipfile.ZipFile(nupkg, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("_rels/.rels", f'''<?xml version="1.0" encoding="utf-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Type="http://schemas.microsoft.com/packaging/2010/07/manifest" Target="/{ident}.nuspec" Id="R{uuid.uuid4().hex[:16].upper()}" />
  <Relationship Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="/package/services/metadata/core-properties/{psm}.psmdcp" Id="R{uuid.uuid4().hex[:16].upper()}" />
</Relationships>''')
    z.writestr(f"{ident}.nuspec", re.sub(r"\s*<files>.*?</files>", "", spec, flags=re.S))
    for f in sorted(pathlib.Path("tools").iterdir()):
        z.write(f, f"tools/{f.name}")
    z.writestr("[Content_Types].xml", '''<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml" /><Default Extension="nuspec" ContentType="application/octet" /><Default Extension="txt" ContentType="application/octet" /><Default Extension="exe" ContentType="application/octet" /><Default Extension="psmdcp" ContentType="application/vnd.openxmlformats-package.core-properties+xml" /></Types>''')
    z.writestr(f"package/services/metadata/core-properties/{psm}.psmdcp", f'''<?xml version="1.0" encoding="utf-8"?>
<coreProperties xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.openxmlformats.org/package/2006/metadata/core-properties">
  <dc:creator>{escape(get("authors"))}</dc:creator>
  <dc:description>{escape(desc)}</dc:description>
  <dc:identifier>{ident}</dc:identifier>
  <version>{ver}</version>
  <keywords>{escape(get("tags"))}</keywords>
  <lastModifiedBy>emaki-choco pack.py</lastModifiedBy>
</coreProperties>''')
print(nupkg)
