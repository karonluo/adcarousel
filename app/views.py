from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Adcarousel
import os
from django.conf import settings
from django.http import JsonResponse
import logging
from .models import Adcarousel
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
import uuid
import re
from django.utils import timezone


logger = logging.getLogger(__name__)
def adcarousel(request):
    adcarousels = Adcarousel.objects.all().order_by('-isselected','orderkey')
    
    return render(request, 'adcarousel_list.html', {'adcarousels': adcarousels})


def edit_adcarousel(request):
    adcarousels = Adcarousel.objects.all()
    
    return HttpResponse("OK")


def delete_adcarousel(request):
    adcarousels = Adcarousel.objects.all()
    return HttpResponse("OK")

def adcarousel_detail(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    return render(request, 'adcarousel_detial.html', {'adcarousel': adcarousel})

def upload_file(request):
    if request.method == 'POST': 
        file = request.FILES['file']
        file_path = os.path.join(settings.BASE_DIR, 'app/static/images', file.name)

        # 确保目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 保存文件
        with open(file_path, 'wb') as f:
            f.write(file.read())

        # 返回文件的HTTP地址
        return JsonResponse({
            'url': request.build_absolute_uri(settings.STATIC_URL + 'images/' + file.name)
        })
    else:
        return HttpResponse('Only POST method is allowed')
    
    


MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}


def adcarousel_create(request):
    if request.method=="GET":
        print("Hello")
    if request.method == 'POST':
        adcarousel = Adcarousel()
        adcarousel.id = str(uuid.uuid4()).replace("-","_")  # 生成 UUID
        if 'picpath' in request.FILES:
            file = request.FILES['picpath']
            ext = os.path.splitext(file.name)[1]  # 获取文件后缀
            new_filename = f"{uuid.uuid4()}{ext}"  # 使用随机 UUID 重命名文件
            file_path = os.path.join(settings.MEDIA_ROOT, new_filename)
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            adcarousel.picpath = settings.MEDIA_URL + new_filename
        
        showtimeout = request.POST.get('showtimeout')
        if int(showtimeout) < 5:
            messages.error(request, '显示秒数不能小于5秒')
            return render(request, 'adcarousel_detial.html', {'adcarousel': adcarousel})

        fontposition = request.POST.get('fontposition')
        regex = r'^\d+,\d+$'
        if not re.match(regex, fontposition):
            messages.error(request, '文字位置格式不正确，请输入 "x,y" 格式的值')
            return render(request, 'adcarousel_detial.html', {'adcarousel': adcarousel})

        adcarousel.showtimeout = showtimeout
        adcarousel.fontcolor = request.POST.get('fontcolor')
        adcarousel.fontposition = fontposition
        adcarousel.fontsize = request.POST.get('fontsize')
        adcarousel.isselected = int(request.POST.get('isselected'))
        adcarousel.createby = 'admin'
        adcarousel.createat = timezone.now()
        adcarousel.updateby = 'admin'
        adcarousel.updateat = timezone.now()
        adcarousel.orderkey = 0
        adcarousel.save()
        messages.success(request, '新增成功')
        return redirect('adcarousel_detail', id=adcarousel.id)
    elif request.method == 'GET':
        return render(request, 'adcarousel_detial.html', {'adcarousel': None, 'now': timezone.now()})



def adcarousel_update(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    if request.method == 'POST':
        if 'picpath' in request.FILES:
            file = request.FILES['picpath']
            ext = os.path.splitext(file.name)[1]  # 获取文件后缀
            new_filename = f"{uuid.uuid4()}{ext}"  # 使用随机 UUID 重命名文件
            file_path = os.path.join(settings.MEDIA_ROOT, new_filename)
            logger.info(f"Saving file to {file_path}")
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            adcarousel.picpath = settings.MEDIA_URL + new_filename
        
        showtimeout = request.POST.get('showtimeout')
        if int(showtimeout) < 5:
            messages.error(request, '显示秒数不能小于5秒')
            return render(request, 'adcarousel_detial.html', {'adcarousel': adcarousel})

        fontposition = request.POST.get('fontposition')
        regex = r'^\d+,\d+$'
        if not re.match(regex, fontposition):
            messages.error(request, '文字位置格式不正确，请输入 "x,y" 格式的值')
            return render(request, 'adcarousel_detial.html', {'adcarousel': adcarousel})

        adcarousel.showtimeout = showtimeout
        adcarousel.fontcolor = request.POST.get('fontcolor')
        adcarousel.fontposition = fontposition
        adcarousel.fontsize = request.POST.get('fontsize')
        adcarousel.isselected = int(request.POST.get('isselected'))
        adcarousel.updateby = 'admin'
        adcarousel.updateat = timezone.now()
        adcarousel.save()
        messages.success(request, '保存成功')
        return redirect('adcarousel_detail', id=adcarousel.id)
    return render(request, 'adcarousel_detial.html', {'adcarousel': adcarousel, 'now': timezone.now()})



def delete_adcarousel(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    # 获取文件路径
    file_path = os.path.join(settings.MEDIA_ROOT, os.path.basename(adcarousel.picpath))
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            logger.info(f"Deleted file: {file_path}")
        except Exception as e:
            logger.error(f"Error deleting file: {e}")
    adcarousel.delete()
    messages.success(request, '删除成功')
    return JsonResponse({'message': '删除成功'})

def adcarousel_detail(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    return render(request, 'adcarousel_detial.html', {'adcarousel': adcarousel})

def adcarousel_preview(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    
    font_position = adcarousel.fontposition.split(',')
    context = {
        'adcarousel': adcarousel,
        'font_position_x': font_position[0],
        'font_position_y': font_position[1],
    }
    return render(request, 'adcarousel_preview_setdatetimepostion.html', context)
def adcarousel_preview1(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    
    font_position = adcarousel.fontposition.split(',')
    context = {
        'adcarousel': adcarousel,
        'font_position_x': font_position[0],
        'font_position_y': font_position[1],
    }
    return render(request, 'adcarousel_preview.html', context)
    # return render(request, 'adcarousel_preview.html', {'adcarousel': adcarousel})


@csrf_exempt
# @require_POST
def toggle_is_selected(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    is_selected = request.POST.get('is_selected') == 'true'
    adcarousel.isselected = int(is_selected)  # 将布尔值转换为整数
    adcarousel.save()
    return JsonResponse({'message': '状态更新成功'})


def adcarousel_list_play(request):
    adcarousels = Adcarousel.objects.filter(isselected=1).order_by('orderkey')
    
    # 预处理 fontposition 数据
    for adcarousel in adcarousels:
        font_position = adcarousel.fontposition.split(',')
        adcarousel.font_position_x = font_position[0]
        adcarousel.font_position_y = font_position[1]
    
    return render(request, 'adcarousel_list_play.html', {'adcarousels': adcarousels})


@csrf_exempt
# @require_POST
def adcarousel_create(request):
    if request.method == 'POST':
        adcarousel = Adcarousel()
        adcarousel.id = str(uuid.uuid4()).replace("-","_")  # 生成 UUID
        if 'picpath' in request.FILES:
            file = request.FILES['picpath']
            ext = os.path.splitext(file.name)[1]  # 获取文件后缀
            new_filename = f"{uuid.uuid4()}{ext}"  # 使用随机 UUID 重命名文件
            file_path = os.path.join(settings.MEDIA_ROOT, new_filename)
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            adcarousel.picpath = settings.MEDIA_URL + new_filename
        
        showtimeout = request.POST.get('showtimeout')
        if int(showtimeout) < 5:
            messages.error(request, '显示秒数不能小于5秒')
            return render(request, 'adcarousel_detial.html', {'adcarousel': adcarousel})

        adcarousel.showtimeout = showtimeout
        adcarousel.fontcolor = request.POST.get('fontcolor')
        adcarousel.fontposition = request.POST.get('fontposition')
        adcarousel.fontsize = request.POST.get('fontsize')
        adcarousel.isselected = int(request.POST.get('isselected'))
        adcarousel.createby = 'admin'
        adcarousel.createat = timezone.now()
        adcarousel.updateby = 'admin'
        adcarousel.updateat = timezone.now()
        adcarousel.orderkey = 0
        adcarousel.save()
        messages.success(request, '新增成功')
        return redirect('adcarousel_detail', id=adcarousel.id)
    return render(request, 'adcarousel_detial.html', {'adcarousel': None})



@csrf_exempt
# @require_POST
def update_orderkey(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    orderkey = request.POST.get('orderkey')
    if orderkey.isdigit():
        adcarousel.orderkey = int(orderkey)
        adcarousel.save()
        return JsonResponse({'message': '顺序更新成功'})
    else:
        return JsonResponse({'message': '顺序更新失败：请输入有效的整数'}, status=400)
    
    
@csrf_exempt
# @require_POST
def update_fontcolor(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    fontcolor = request.POST.get('fontcolor')
    adcarousel.fontcolor = fontcolor
    adcarousel.save()
    return JsonResponse({'message': '文字颜色更新成功'})

@csrf_exempt
# @require_POST
def update_fontsize(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    fontsize = request.POST.get('fontsize')
    if fontsize.isdigit():
        adcarousel.fontsize = int(fontsize)
        adcarousel.save()
        return JsonResponse({'message': '文字大小更新成功'})
    else:
        return JsonResponse({'message': '文字大小更新失败：请输入有效的整数'}, status=400)


@csrf_exempt
# @require_POST
def update_fontposition(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    fontposition = request.POST.get('fontposition')
    regex = r'^\d+,\d+$'
    if not re.match(regex, fontposition):
        return JsonResponse({'message': '文字位置格式不正确，请输入 "x,y" 格式的值'}, status=400)
    adcarousel.fontposition = fontposition
    adcarousel.save()
    return JsonResponse({'message': '文字位置更新成功'})

@csrf_exempt
# @require_POST
def update_showtimeout(request, id):
    adcarousel = get_object_or_404(Adcarousel, id=id)
    showtimeout = request.POST.get('showtimeout')
    if showtimeout:
        adcarousel.showtimeout = int(showtimeout)
        adcarousel.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid showtimeout'}, status=400)