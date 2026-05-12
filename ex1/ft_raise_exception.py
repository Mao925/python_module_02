# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhashimo <mhashimo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/12 22:37:33 by mhashimo          #+#    #+#              #
#    Updated: 2026/05/12 22:47:52 by mhashimo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp

def test_temperature() -> None:
	for s in ["25", "abc", "100", "-50"]:
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
	print("All test completed - program didn't crash!")

if __name__ == "__main__":
	main()
