from django.shortcuts import render

def index(request):
    context = {
        'title': 'Store',
        'sale': 'Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'is_sale': False,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Catalog',
        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'cardtitle': 'Худи черного цвета с монограммами adidas Originals',
                'price': '6 090',
                'cardtext': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
            {
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'cardtitle': 'Синяя куртка The North Face',
                'price': '23 725',
                'cardtext': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
            },
            {
                'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'cardtitle': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': '3 390',
                'cardtext': 'Материал с плюшевой текстурой. Удобный и мягкий.',
            },
            {
                'image': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
                'cardtitle': 'Черный рюкзак Nike Heritage',
                'price': '2 340',
                'cardtext': 'Плотная ткань. Легкий материал.',
            },
            {
                'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
                'cardtitle': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': '13 590',
                'cardtext': 'Гладкий кожаный верх. Натуральный материал.',
            },
            {
                'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'cardtitle': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': '2 890',
                'cardtext': 'Гладкий кожаный верх. Натуральный материал.',
            },
        ]
    }
    return render(request, 'products/products.html', context)
