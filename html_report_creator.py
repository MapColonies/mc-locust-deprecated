import os

os.system(r"locust -f playground.py -u 1 -r 1 -t 10s --headless --print-stats --host=https://localhost --html test.html")

import bs4


# load the file

def open_xml_file(file_path):
    with open(file_path) as xml_doc:
        txt = xml_doc.read()
        soup = bs4.BeautifulSoup(txt)
        return soup


def add_new_tag(soup, tag_data):
    # create new link
    new_tag = soup.new_tag(tag_data)
    # insert it into the document
    soup.head.append(new_tag)


# save the file again
def save_file_changes(file_path, updates):
    with open(file_path, "w") as changes:
        changes.write(str(updates))
