import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# -------------------------------
# STEP 1: Create Dataset
# -------------------------------
data = {
    'Balance': [1000, 2000, 3000, 4000, 5000, 6000, 7000],
    'Withdraw': [500, 2500, 1000, 4500, 2000, 6500, 3000],
    'Status':   [1,    0,    1,    0,    1,    0,    1]  # 1=Success, 0=Fail
}

df = pd.DataFrame(data)

# -------------------------------
# STEP 2: Train Model
# -------------------------------
X = df[['Balance', 'Withdraw']]
y = df['Status']

model = DecisionTreeClassifier()
model.fit(X, y)

# -------------------------------
# STEP 3: User Input
# -------------------------------
balance = int(input("Enter Account Balance: "))
withdraw = int(input("Enter Withdrawal Amount: "))

# -------------------------------
# STEP 4: Prediction
# -------------------------------
prediction = model.predict([[balance, withdraw]])

if prediction[0] == 1:
    print("✅ Transaction Likely SUCCESS")
else:
    print("❌ Transaction Likely FAIL")

# -------------------------------
# STEP 5: Graph Output
# -------------------------------
colors = ['green' if s == 1 else 'red' for s in df['Status']]

plt.scatter(df['Balance'], df['Withdraw'], c=colors)
plt.xlabel("Balance")
plt.ylabel("Withdrawal Amount")
plt.title("ATM Prediction Model")

plt.grid()
plt.show()
