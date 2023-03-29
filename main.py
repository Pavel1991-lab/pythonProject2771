from classes import Shop, Store, Request

store = Store(
    items = {"Печеньки": 34,
            "Хлеб": 12,
             "Конфеты": 2,
             "Дыня": 11,
             "Капуста": 23,
             "Апельсин": 4}
)



shop = Shop(
    items = {"Печеньки": 2,
             "Хлеб": 1,
             "Конфеты": 1
             }
)


storages = {
    'магазин': shop,
    'склад': store
}

def main():
    print('Добрый день')

    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')
        user = input("Куда будем везти?")
        if user.lower() == 'магазин':

                for storage_name in storages:
                    print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')
                user_input = input(
                    'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
                    'Введите стоп или stop если хотите закончить:\n')

                if user_input in ('stop', 'стоп'):
                    break

                request = Request(request=user_input)

                if request.depature in storages and request.destination in storages:
                    storages[request.depature].remove(request.product, request.amount)
                    print(f'Курьер забрал {request.amount} {request.product} в {request.depature}')
                    storages[request.destination].add(request.product, request.amount)
                    print(f'Курьер доставил {request.amount} {request.product} в {request.destination}')
                else:
                    print("Некорректный запрос")


        elif user.lower() == 'склад':

                for storage_name in storages:
                    print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')
                user_input = input(
                    'Введите запрос в формате "Доставить 3 печеньки из магазин в склад"\n'
                    'Введите стоп или stop если хотите закончить:\n')

                if user_input in ('stop', 'стоп'):
                    break

                request = Request(request=user_input)

                if request.depature in storages and request.destination in storages:
                    storages[request.depature].remove(request.product, request.amount)
                    print(f'Курьер забрал {request.amount} {request.product} в {request.depature}')
                    storages[request.destination].add(request.product, request.amount)
                    print(f'Курьер доставил {request.amount} {request.product} в {request.destination}')
                else:
                    print("Некорректный запрос")



        elif user.lower() in {'стоп', 'stop'}:
            break

        else:
            print('Некоректный запрос')
main()
