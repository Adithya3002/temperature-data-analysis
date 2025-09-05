import os
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

class TemperatureSummaryView(View):
    def get(self, request):
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temperature_data.csv')
        df = pd.read_csv(csv_path)
        summary = {
            'avg_temp': round(df['AvgTemperature'].mean(), 2),
            'states': df['State'].nunique(),
            'months': df['Month'].nunique(),
            'years': df['Year'].nunique()
        }
        return JsonResponse(summary)

def temperature_by_state(request):
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temperature_data.csv')
    df = pd.read_csv(csv_path)
    state_avg = df.groupby('State')['AvgTemperature'].mean().reset_index()
    return JsonResponse({'temperature_by_state': state_avg.to_dict(orient='records')})

def monthly_temperature_trend(request):
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temperature_data.csv')
    df = pd.read_csv(csv_path)
    trend = df.groupby(['Year', 'Month'])['AvgTemperature'].mean().reset_index()
    trend['YearMonth'] = trend['Year'].astype(str) + '-' + trend['Month']
    return JsonResponse({'monthly_trend': trend[['YearMonth', 'AvgTemperature']].to_dict(orient='records')})

# Render Pages
def temperature_summary_page(request):
    return render(request, 'descriptive/temperature_summary.html')

def temperature_by_state_page(request):
    return render(request, 'descriptive/temperature_by_state.html')

def temperature_trend_page(request):
    return render(request, 'descriptive/temperature_trend.html')

#new   

def overall_dashboard(request):
    return render(request, 'descriptive/overall_dashboard.html')

