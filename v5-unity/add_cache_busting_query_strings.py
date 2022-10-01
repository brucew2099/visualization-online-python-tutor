# add cache-busting query strings for build/*.js files referenced by all html
# files in the current directory

import os, re, hashlib

PREFIX = 'src="'
SUFFIX = '"'

STUFF_RE = re.compile(f'{PREFIX}(build/.*[.]js).*?{SUFFIX}')

import os, re, hashlib

for f in os.listdir('.'):
  if f.endswith('.html'):
    new_f = f'{f}.NEW'
    with open(new_f, 'w') as out:
      for line in open(f):
        if m := STUFF_RE.search(line):
          js_filename = m[1]
          assert os.path.isfile(js_filename)
          md5_hash = hashlib.md5(open(js_filename, 'rb').read()).hexdigest()
          md5_hash = md5_hash[:10] # truncate to prettify
          modified_line = re.sub(STUFF_RE, 'src="' + js_filename + '?' + md5_hash + SUFFIX, line)
          js_filename = m.group(1)
          out.write(modified_line)
        else:
          out.write(line)

    os.rename(new_f, f)
