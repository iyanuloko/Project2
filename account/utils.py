import random

def GeneratePin():
	"""
		TO Generate Pin for Confirmation
	"""
	pin = ""
	for i in range(1, 5):
		pin += str(random.randint(1,9));
	return pin

def upload_location(instance, filename):
    file_path = 'students/{student_id}/Photo/{filename}'.format(
        student_id=str(instance.matric_no), filename=str(GeneratePin()+".jpg"))
    return file_path


