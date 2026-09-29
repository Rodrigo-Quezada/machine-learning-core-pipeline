import argparse
from src.dataset_manager import DataPipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
def main():
    # configuracion de argumentos por linea de comandos (logica avanzada de terminal)
    parser=argparse.ArgumentParser(description="Pipeline de ML de Alto Rendimiento para Startups")
    parser.add_argument("--samples",type=int,default=1000,help="Numero de muestras a procesar")
    parser.add_argument("--features",type=int,default=12,help="Numero de caracteristicas dimensionales")
    parser.add_argument("--output",type=str,default="reporte_operaciones.xlsx",help="Nombre del archivo Excel de salida")
    args=parser.parse_args()
    print("[START] iniciando pipeline de procesamiento")
    # 1. Pipeline de datos
    pipeline=DataPipeline(num_samples=args.samples,num_features=args.features)
    X_raw,y=pipeline.generate_synthetic_data()
    X=pipeline.normalize_features(X_raw)
    # 2. Division de datos Temporal/Espacial
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    # 3. Modelamiento predictivo
    print("[MODEL] Entrenando clasificador de optimizacion")
    model=RandomForestClassifier(n_estimators=100,random_state=42,n_jobs=-1) # manejo de concurrencia
    model.fit(X_train,y_train)
    # 4. Evaluacion metricas tecnicas
    predictions=model.predict(X_test)
    print("[RESULTADOS] Reporte de rendimiento tecnico: ")
    print(classification_report(y_test,predictions))
    # Reporte en formato de diccionario estructurado para su exportacion
    reporte_dict=classification_report(y_test,predictions,output_dict=True)
    # 5. Automatizacion de entrega de resultados
    pipeline.export_metrics_to_excel(reporte_dict, args.output)
    print("[END] Ejecucion pipeline terminada")
if __name__=="__main__":
    main()