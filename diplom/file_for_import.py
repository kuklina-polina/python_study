from read_write_data import read_mapinfo_tab, create_entry_fields
import tkinter as tk
from tkinter import ttk
from sqlalchemy import create_engine
import pandas as pd

class OrthoForImport():
    def __init__(self, type, filepath, conn):
        self.type = type
        self.path = filepath
        self.data = read_mapinfo_tab(self.path)
        self.schema_name = self.type
        self.conn = conn

    def preprocessing(self, data):
        input_list = ["Шифр", "Владелец", "Примечание", "Расположение", "Дата создания"]
        self.param_dop = create_entry_fields(input_list)

        return self.pre_ortho(data)


    def pre_ortho(self, data):
        data_to_import = data.rename(columns={'Название_файла_ЦОФП': 'name',
                                              'Дата_съемки_ггггммдд': 'date_sourc',
                                              'Масштаб': 'scale',
                                              'Разрешение_м': 'resolution',
                                              # 'Полнота_покрытия_%': 'coverage',
                                              'Облачность_%': 'cloud_cove',
                                              'Гриф_секретности': 'secret',
                                              'Формат': 'format',
                                              'Исполнитель_ЦОФП': 'executor',
                                              'Примечание': 'notes',
                                              'Госконтракт_номер_дата': 'contract'})
        data_to_import = data_to_import.set_crs("epsg:7683", allow_override=True)
        data_to_import = data_to_import.drop_duplicates('geometry')
        data_to_import = data_to_import.drop(columns=['ID_папки',
                                      'Исх_материал',
                                      'Вид_изображения',
                                      'Качество_%',
                                      'Точность_план_м',
                                      'Субъект_РФ',
                                      'Система_координат',
                                      'ОТК_заключение',
                                                      'Полнота_покрытия_%'], axis=0)

        # data_to_import['scale'] = data_to_import['scale'].replace(" ", "")
        data_to_import['scale'] = data_to_import['scale'].replace("10 000", "10000")
        data_to_import['scale'] = data_to_import['scale'].replace("2 000", "2000")

        format_dict = self.conn.get_format()
        data_to_import['format'] = data_to_import['format'].map(format_dict)

        data_to_import['executor'] = 'Аэрогеодезия'
        company_dict = self.conn.get_companies()
        data_to_import['executor'] = data_to_import['executor'].map(company_dict)

        data_to_import['owner'] = self.param_dop["Владелец"]
        company_dict = self.conn.get_companies()
        data_to_import['owner'] = data_to_import['owner'].map(company_dict)

        data_to_import['notes'] = self.param_dop["Примечание"]
        data_to_import['cassette_number'] = self.param_dop["Расположение"]
        data_to_import['date_creat'] = self.param_dop["Дата создания"]

        secret_dict = self.conn.get_secret()
        data_to_import['secret'] = data_to_import['secret'].map(secret_dict)

        data_to_import['contract'] = self.param_dop["Шифр"]
        contract_dict = self.conn.get_contract()
        data_to_import['contract'] = data_to_import['contract'].map(contract_dict)

        data_to_import = data_to_import.apply(lambda x: pd.to_numeric(x, errors='coerce') if x.name in ["scale","format","executor",
         "contract", "secret", "cloud_cove", "resolution", "cloud_cove"] else x)

        data_to_import['geometry'] = data_to_import["geometry"].buffer(0)
        data_to_import = data_to_import.dropna(subset=['geometry'])

        data_to_import['date_creat'] = pd.to_datetime(data_to_import['date_creat'] , format='%Y%m%d', errors='coerce')
        data_to_import['date_sourc'] = pd.to_datetime(data_to_import['date_sourc'] , format='%Y%m%d', errors='coerce')
        return data_to_import