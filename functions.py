#Meal Time
def meal_time(TimeString):
  hours, minutes, seconds = TimeString.split(":")

  hours = int(hours)
  minutes = int(minutes)
  seconds = int(seconds)

  if hours >= 7 and hours <= 8:
    return "breakfast"
  elif hours >= 12 and hours <= 13:
    return "lunch"
  elif hours >=18 and hours <= 19:
    return "dinner"
  else:
    return "nothing right now"

print("7:00:00 =>", meal_time("7:00:00"))
print("12:00:00 =>", meal_time("12:00:00"))
print("18:00:00 =>", meal_time("18:00:00"))
print("19:00:00 =>", meal_time("19:00:00"))
print("21:00:00 =>", meal_time("21:00:00"))


#Get filename extension
def get_filename_extension(filename):
  name, extension = filename.split(".")

  return extension

print("hello.jpg =>", get_filename_extension("hello.jpg"))
print("hello.py =>", get_filename_extension("hello.py"))


#Is Image File
def is_image_file(filename):
  name, extension = filename.split(".")
  
  if extension == "jpg" or extension == "jpeg" or extension == "png" or extension == "gif" or extension == "tiff":
    return True
  else:
    return False

print("hello.jpg =>", is_image_file("hello.jpg"))
print("hello.png =>", is_image_file("hello.png"))
print("hello.csv =>", is_image_file("hello.csv"))