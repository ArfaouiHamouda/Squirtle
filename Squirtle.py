import os,shutil,random
import requests
import json
import csv
from collections import OrderedDict
from bs4 import BeautifulSoup

class Squirtle:
    file_name = 'Squirtle.csv'
    dir = 'downloads'
    max_pages = 0
    limit_per_page = None
    page_url = ""
    item_selector = ''
    fields = OrderedDict([])
    isDownload = False

    def generate_csv(self):
        page = 1
        count = 0
        if os.path.isdir(self.dir) is True:
            shutil.rmtree(self.dir)
        os.mkdir(self.dir)
        with open(self.file_name, 'w', newline='') as file:
            headers = ['ID'] + list(self.fields.keys()) + ['link']
            db = csv.DictWriter(file, fieldnames=headers)
            db.writeheader()
            while page <= self.max_pages:
                url = self.page_url + str(page)
                soup = BeautifulSoup(requests.get(url).text, "html.parser")

                for item in soup.select(self.item_selector, limit=self.limit_per_page):
                    count = count + 1
                    db = csv.writer(file)
                    db.writerow(self.get_single_item_data(item.get('href'), self.isDownload,count))

                page += 1

    def get_single_item_data(self,item_url,download, count):
        soup = BeautifulSoup(requests.get(item_url).text, "html.parser")
        print('Generating Item N#'+str(count))
        data = []
        data.append(str(count))
        for key in self.fields:
            item = soup.select_one(self.fields[key])
            if item is not None:
                if item.name == 'img':
                    if download is True:
                        data.append(self.save_file(item['src']))
                    else:
                        data.append(item['src'])
                else:
                    data.append(item.text)
            else:
                data.append('')
        data.append(item_url)
        return data

    def generate_json(self):
        self.file_name = 'Squirtle.json'
        if os.path.isdir(self.dir) is True:
            shutil.rmtree(self.dir)
        os.mkdir(self.dir)
        with open(self.file_name, 'w', newline='') as file:
            json.dump(self.get_json(self.isDownload),file)

    def get_json(self,download):
        page = 1
        headers = list(self.fields.keys()) + ['link']
        output = []
        while page <= self.max_pages:
            url = self.page_url + str(page)
            soup = BeautifulSoup(requests.get(url).text, "html.parser")
            for item in soup.select(self.item_selector, limit=self.limit_per_page):
                output.append(self.get_single_item_json(item.get('href'),download))
            page += 1
        return output

    # Function return Dictionary of wanted Values of Specific Element item_url
    def get_single_item_json(self,item_url,download):
        soup = BeautifulSoup(requests.get(item_url).text, "html.parser")
        data = {}
        for key in self.fields:
            item = soup.select_one(self.fields[key])
            if item is not None:
                if item.name == 'img':
                    if download is True:
                        data[key] = self.save_file(item['src'])
                    else:
                        data[key] = item['src']
                else:
                    data[key] = item.text
            else:
                data[key] = ''
        data['link'] = item_url
        return data

    def save_file(self,src):
        filename, file_extension = os.path.splitext(os.path.basename(src))
        filename = random.getrandbits(128)
        with open(self.dir+'/'+str(filename)+file_extension, 'wb') as handle:
            response = requests.get(src, stream=True)
            if not response.ok:
                return response
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
            return str(filename)+file_extension

