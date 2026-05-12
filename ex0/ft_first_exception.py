# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhashimo <mhashimo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/12 21:59:49 by mhashimo          #+#    #+#              #
#    Updated: 2026/05/12 22:47:31 by mhashimo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(temp_str) -> int:
	return int(temp_str)

def test_temperature() -> None:
	for s in ["25", "abc"]:
		print()
		print(f"Input data is '{s}'")
		try:
			temp = input_temperature(s)
			print(f"Temperature is now {temp}°C")
		except Exception as e:
			print(f"Caught input_temperature error: {e}")

def main() -> None:
	print("=== Garden Temperature ===")
	test_temperature()
	print()
	print("All test completed - program didn't  crash!")

if __name__ == "__main__":
	main()
