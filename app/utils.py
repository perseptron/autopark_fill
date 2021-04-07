import zipfile

import requests


def download(url, file, **kwargs):
    progress = kwargs.get('progress', None)
    prev = 0
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total = int(r.headers['content-length'])  # <- ptb probably already knows "size"
        with open(file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    if progress:
                        cur = round(f.tell()/total*100)
                        if cur - prev > 0.5:
                            progress(cur, total)  # <- added callback
                            prev = cur


def unzip(file_path, **kwargs):
    progress = kwargs.get('progress', None)
    zf = zipfile.ZipFile(file_path)
    uncompress_size = sum((file.file_size for file in zf.infolist()))
    extracted_size = 0
    for file in zf.infolist():
        extracted_size += file.file_size
        if progress:
            progress(extracted_size, uncompress_size)
        zf.extract(file)
    return zf.infolist()


def get_lines_count(file_path):
    print('counting...')
    count = 0
    thefile = open(file_path, 'rb')
    while 1:
        buffer = thefile.read(8192 * 1024)
        if not buffer: break
        count += buffer.count(b'\n')
    thefile.close()
    return count