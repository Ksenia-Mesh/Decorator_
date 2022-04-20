from datetime import datetime
import os

def file(file_name, file_path=None):
	if file_path is None:
		file_place = os.path.join(os.getcwd())
	else:
		file_place = os.path.join(os.path.abspath(file_path))

	file_path = os.path.join(file_place, file_name)

	def decor(foo):

		def new_foo(*args, **kwargs):
			now_date = datetime.today()
			name = foo.__name__
			arguments = f'Аргументы:{args} и {kwargs}'
			result = foo(*args, **kwargs)
			result_line = f'Вызов функции в: {now_date} \n' \
						  f'Функция: {name} \n' \
						  f'{arguments} \n' \
						  f'Возвращаемое значение: {result}\n' \
						  f'Окончание работы\n'


			with open(file_path, 'a', encoding='utf-8') as f:
				f.write(result_line)

			return result

		return new_foo

	return decor


