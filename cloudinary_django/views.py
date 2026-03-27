from django.http import JsonResponse
import cloudinary.uploader
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_3d_model(request):
    if request.method == 'POST' and request.FILES['file']:
        archivo_3d = request.FILES['file']
        
        try:
            # Subida directa a Cloudinary
            resultado = cloudinary.uploader.upload(
                archivo_3d,
                resource_type = "raw",
                folder = "modelos_3d/",
                public_id = archivo_3d.name # Opcional: mantener el nombre original
            )
            
            # La URL estará en resultado['secure_url']
            return JsonResponse({"url": resultado['secure_url']}, status=200)
            
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "No POST method or no file uploaded"}, status=400)