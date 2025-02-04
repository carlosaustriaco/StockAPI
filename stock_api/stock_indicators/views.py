from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .utils import fetch_data

class IndicatorAPI(View):
    def get(self, request):
        symbol = request.GET.get('symbol', '').upper()
        indicator = request.GET.get('indicator', '').lower()

        if (not symbol) and (not indicator):
            return JsonResponse({'error': 'Missing "symbol" and "indicator" parameter'}, status=400)
        
        only_symbol = symbol and (not indicator)

        try:
            if only_symbol:
                stock_data = fetch_data(symbol)
                last_close = stock_data['Close'].iloc[-1]
                return JsonResponse({'symbol': symbol, 'close' : f"{last_close:.2f}"})
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
