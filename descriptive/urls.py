from django.urls import path
from .views import (
    TemperatureSummaryView, temperature_by_state, monthly_temperature_trend,
    temperature_summary_page, temperature_by_state_page, temperature_trend_page,
    overall_dashboard  # ✅ Add this!
)

urlpatterns = [
    path('', temperature_summary_page, name='home'),
    path('summary/', temperature_summary_page, name='temperature-summary'),
    path('temperature_by_state/', temperature_by_state_page, name='temperature-by-state'),
    path('temperature_trend/', temperature_trend_page, name='temperature-trend'),
    path('api/summary/', TemperatureSummaryView.as_view(), name='temperature-summary-api'),
    path('api/temperature_by_state/', temperature_by_state, name='temperature-by-state-api'),
    path('api/monthly_trend/', monthly_temperature_trend, name='temperature-trend-api'),

    path('dashboard/', overall_dashboard, name='overall-dashboard'),

]
