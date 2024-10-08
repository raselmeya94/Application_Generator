from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import utils

@csrf_exempt
def nothi_application_generator(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            model_name = data.get('model')
            question = data.get('question')
            
            if not model_name or not question:
                return JsonResponse({"status": "error", "error": "Model name and question are required"}, status=400)

            # Generate application code based on the model name and questions
            answer = utils.get_answer(model_name, question)
            
            if answer is None:
                return JsonResponse({"status": "error", "error": "Failed to generate response"}, status=500)

            return JsonResponse({"status": "success", "response": answer}, status=200)  # Explicitly setting status to 200
        
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "error": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "error": "Invalid request method"}, status=405)
