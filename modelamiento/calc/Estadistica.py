import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

class Estadistica:

    def __init__(self):
        self.df = pd.read_excel('info/dataset.xlsx')
    
    def datosExcel(self):

        return self.df

    def graficoFrecuenciaDelPrecioMaximoAlcanzado(self):

        img = io.BytesIO()

        cliente = self.df['Volúmen']
        plt.figure(figsize=(10,5))
        plt.hist(cliente, bins=None, color='green')
        plt.title('Frecuencia del volúmen')
        plt.xticks(rotation=10)
        plt.ylabel('Frecuencia')
        plt.xlabel('volúmen')

        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url
