from flask import Flask, render_template
import matplotlib.pyplot as plt
import base64
from io import BytesIO

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ml')
def machine():


    # Step 1: Create a simple Matplotlib plot
    plt.figure(figsize=(6, 4))
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], label="x^2", color='blue')
    plt.title("Example Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()

    # Step 2: Save the plot to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')  # Save the plot tightly cropped
    buffer.seek(0)  # Move the buffer pointer to the beginning

    # Step 3: Convert the buffer to a Base64 string
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Step 4: Create a data URI from the Base64 string
    data_uri = f"data:image/png;base64,{image_base64}"



    return render_template('graph.html', html_data_uri=data_uri)

if __name__ == '__main__':
    app.run(debug=True)