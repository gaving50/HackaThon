from flask_backend import app;

#Grabbing API without disclosing it

# Example usage
if __name__ == "__main__":
    
    try:
        app.run()
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    
    