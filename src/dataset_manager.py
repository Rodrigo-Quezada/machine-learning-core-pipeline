import numpy as np
import pandas as pd
import os
class DataPipeline:
    def __init__(self,num_samples: int=1000,num_features: int=10):
        self.num_samples=num_samples
        self.num_features=num_features
    def generate_synthetic_data(self):
        # carga de tensores/matrices en memoria
        print(f"[INFO] Generar matriz densa de {self.num_samples}x{self.num_features}")
        X=np.random.randn(self.num_samples,self.num_features)
        y=np.random.randint(0,2,size=self.num_samples)
        return X,y 
    def normalize_features(self,X: np.ndarray) -> np.ndarray:
        # normalizacion estadistica estandar (Z-score)
        mean=np.mean(X,axis=0)
        std=np.std(X,axis=0)
        # evitar division por 0 en forma segura
        std[std==0]=1e-8
        return (X-mean)/std
    def export_metrics_to_excel(self,report_dict,filename="reporte_rendimiento.xlsx"):
        # automatizar generacion de reporte en excel, manipulacion de archivos y entrega de resultados
        print("[INFO] Procesando metricas para exportacion con pandas")
        # si reporte queda en tupla se extrae diccionario
        if isinstance(report_dict,tuple):
            report_dict=report_dict[0]
        # extraer 1er elemento tecnico si llega como tupla o lista
        if isinstance(filename,tuple) or isinstance(filename,list):
            filename=filename[0]
        filename=str(filename)
        df=pd.DataFrame(dict(report_dict)).transpose()
        df=df.round(4)
        # output_path=(os.getcwd(),filename)
        output_path=os.path.abspath(str(filename))
        df.to_excel(output_path,index=True,sheet_name="Metricas de IA")
        print(f"[SUCCESS] Reporte de validacion exportado en: {output_path}")
        