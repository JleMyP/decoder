import os, sys


def dec(name, head, fin=None):
  if not fin: fin = open(name, "rb").read()
  start = fin.rfind(head)
  print name[:-9],#, (head,), start
  if start == -1:
      for x in range(len(head)-1, 0, -1):
          if fin[-x:] == head[:x]:
              start = -x
  #print start, len(fin)
  fout = open(os.path.split(name[:-9])[1], "wb")
  fout.write(fin[start:] + fin[:start])
  fout.close()


os.chdir(os.path.dirname(sys.argv[0]))
print sys.argv

exts = (".jpg", ".png", ".pdf", ".rar", ".zip", ".doc", ".docx", ".xlsx", ".gif", ".bmp")
start_jpg = "\xff\xd8\xff"
start_png = "\x89PNG"
start_pdf = "%PDF"
start_rar = "Rar!\x1A\x07"
start_zip = "PK\x03\x04"
start_doc = start_docx = start_zip
start_xlsx = start_zip
start_gif = "GIF8"
start_bmp = "BM"
start_djvu = ""
start_7z = ""


for dirname, dirs, files in os.walk(os.curdir):
  dirname = "" if dirname == "." else (dirname[2:]+"\\").decode("cp1251")
  if "PRIVET.txt" in files: os.remove(dirname+"privet.txt")
  files = [f.lower() for f in files if os.path.splitext(f)[1] == ". hithere"]
  if files:
    try:
      #print dirname.decode('cp1251')
      for f in files:
        ext = os.path.splitext(f.split(". ")[0])[1]
        if ext in exts:
          dec(dirname+f, eval("start_%s"%ext[1:]))
      if raw_input("remove?\n") == "y":
        for f in files: os.remove(dirname+f)
        print "removed"
    except Exception as e:
      print e
