import zipfile
import xml.etree.ElementTree as ET
import glob

with open('output.txt', 'w', encoding='utf-8') as out:
    for f in sorted(glob.glob('b*.docx')):
        try:
            doc = zipfile.ZipFile(f)
            xml_content = doc.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            paragraphs = [node.text for node in tree.findall('.//w:t', ns) if node.text]
            text = ' '.join(paragraphs)
            out.write(f'=== {f} ===\n' + text[:1500] + '\n...\n\n')
        except Exception as e:
            out.write(f'=== {f} ===\nError: {e}\n\n')
