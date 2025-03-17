# Installation and Usage Guide (Linux)

## **Prerequisites**  
Before proceeding, ensure you have the following installed on your system:
- **Git**: To clone the repository
- **Poetry**: To manage dependencies

If you don't have **Poetry**, install it using the following command:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

---

## ** Installation Steps**

### **1️⃣ Clone the Repository**  
Run the following command to clone the project from GitHub:
```bash
git clone git@github.com:MiguelAmato/prueba-tecnica-rauda.git
```

### **2️⃣ Navigate to the Project Directory**  
```bash
cd prueba-tecnica-rauda/
```

### **3️⃣ Set Up Environment Variables**  
Create a `.env` file using the provided template:
```bash
cp .env.template .env
```
Then, **open `.env` and set the appropriate values** for your environment.

### **4️⃣ Install Dependencies**  
Run the following command to install all required dependencies using Poetry:
```bash
poetry install
```

### **5️⃣ Add the CSV File**  
Make sure to place the required CSV file inside the `data/raw` directory:
```bash
mv your_data.csv data/raw/
```

---

## **Usage**

### **1️⃣ Activate the Virtual Environment**  
Before running the script, activate the Poetry environment:
```bash
poetry shell
```

### **2️⃣ Run the Script**  
Execute the main script using:
```bash
poetry run python src/main.py
```

---

## **Additional Notes**
- Ensure that your `.env` file is properly configured before running the script.
- If you face any dependency issues, try running `poetry lock --no-update && poetry install`.
- If Poetry does not detect the environment, try `poetry config virtualenvs.in-project true` and reinstall dependencies.

This guide ensures a smooth installation and execution of the project. 

