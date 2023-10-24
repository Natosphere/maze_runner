from PIL import Image

# Create a sample Pillow image
x = Image.new('RGB', (100, 200), color='red')

def function(x):
    x = x.rotate(90)  # Create a new rotated image, original x remains unchanged
    x.show()

print('before:')
x.show()

function(x)

print('after:')
x.show()