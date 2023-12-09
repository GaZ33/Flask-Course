from market import app

# É necessário utilizar essa abordagem para que a aplicação funcione corretamente
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)