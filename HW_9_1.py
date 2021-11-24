class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self._data = self.__read_file()
        self._result = self._create_res_list()

    def __read_file(self):
        with open(self.filename, "r") as txt_file:
            data = txt_file.readlines()
        return data

    def _create_res_list(self):
        raise NotImplementedError

    @property
    def result_list(self):
        return self._result

    def __repr__(self):
        return f"{self._result}"

class DomainsWorker(FileReader):
    def _create_res_list(self):
        res_list = [name.replace(".", "")[:-1] for name in self._data]
        return res_list

class NamesWorker(FileReader):
    def _create_res_list(self):
        res_list = [surname.split("\t")[1] for surname in self._data]
        return res_list

class ModDateWorker(FileReader):
    _months = {'January': '01',
               'February': '02',
               'March': '03',
               'April': '04',
               'May': '05',
               'June': '06',
               'July': '07',
               'August': '08',
               'September': '09',
               'October': '10',
               'November': '11',
               'December': '12'}

    def __create_split_date_list(self):
        result = []
        for data in self._data:
            data = data.split("-")[0]
            data = data.split()
            if len(data) == 3:
                result.append(data)
        return result

    def _create_res_list(self):
        result = []
        for data in self.__create_split_date_list():
            data_dd = data[0]
            data_dd = data_dd[:-2]
            if len(data_dd) == 1:
                data_dd = "0" + data_dd
            result.append({"date_original": " ".join(data),
                           "date_modified": f"{data_dd}/{self._months.get(data[1])}/{data[2]}"})
        return result


domains_worker = DomainsWorker("domains.txt")
names_worker = NamesWorker("names.txt")
mod_date_worker = ModDateWorker("authors.txt")
