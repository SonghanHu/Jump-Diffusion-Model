# Jump-Diffusion Model README

This README provides an overview of the code implementation for the Jump-Diffusion model. 

### Jump-Diffusion Model (JD)
The Jump-Diffusion model extends the Black-Scholes model by incorporating jumps (sudden, discontinuous movements) in the underlying asset's price. The JD model considers both the continuous diffusion process and the discrete jump process.

##### Key features of the JD model include:

Continuous diffusion process: Captures the gradual, continuous changes in the underlying asset's price over time, similar to the geometric Brownian motion in the Black-Scholes model.
Discrete jump process: Accounts for sudden, discontinuous price movements caused by unforeseen events or news, represented by a Poisson process.
Intensity (λ): Represents the number of jumps per unit of time, indicating the frequency of jump events.
Jump size (m): Represents the mean of the jump size, which can affect the magnitude of the price movements caused by jumps.
Jump volatility (v): Represents the standard deviation of the jump size, capturing the uncertainty or variability in the magnitude of jump movements.
Black-Scholes Model (BS)
The Black-Scholes model is a widely used options pricing model that assumes the underlying asset's price follows a geometric Brownian motion. It provides a theoretical framework for valuing European-style options.

##### Key features of the Black-Scholes model include:

Continuous diffusion process: Assumes that the underlying asset's price follows a log-normal distribution and evolves continuously over time based on a constant volatility (σ).
No consideration of jumps: The Black-Scholes model assumes a continuous price movement without accounting for sudden jumps or discontinuities.
Risk-neutral assumption: Assumes a risk-neutral world, where the expected return on the underlying asset is the risk-free rate (r).
Closed-form solution: Provides a formula to calculate the fair value of European options based on the input parameters (stock price, strike price, time to expiration, risk-free rate, and volatility).
Similarities and Differences
Both JD and BS are used for options pricing and involve modeling the underlying asset's price movement.
JD extends the BS model by incorporating jumps, which can capture sudden and unpredictable price movements.
The BS model assumes a continuous diffusion process, while JD incorporates both continuous diffusion and discrete jump processes.
JD introduces additional parameters (intensity, jump size, jump volatility) to account for the jump process, which are not present in the BS model.
The Black-Scholes model provides closed-form solutions for option pricing, while the JD model typically requires numerical methods or simulations.




Below is a breakdown of the code:

### Step 1: Import Required Libraries

The necessary libraries are imported at the beginning of the code, including `pandas`, `numpy`, `yfinance`, `datetime`, `openpyxl`, `sklearn`, and `torch`.

### Step 2: Define Classes and Functions

The code defines three classes: `get_sigma`, `BlackScholes`, and `JumpDiffusion`, which handle the calculations and computations related to the Jump-Diffusion model.

The code also includes several utility functions, such as `get_ticker`, `get_stock`, `get_call`, `get_call_by_ticker`, `get_full_data`, and `get_daily_change`, which retrieve and process the required data for the model.

The `work` class is the main class that performs the simulation and comparison for different parameters in the Jump-Diffusion model.

### Step 3: Data Preparation

The code retrieves the required data using the utility functions. The historical stock data and option call data are obtained for the specified tickers. The data is then processed and prepared for further analysis.

### Step 4: Normalization

The input data (`X`) is normalized using the `MinMaxScaler` from scikit-learn. The feature range is set to -1 to 1.

### Step 5: Convert Data to Tensors

The normalized data is converted to PyTorch tensors using `torch.tensor`. The input data and target data are reshaped to match the expected input shape of the LSTM model.

### Step 6: Define and Train the LSTM Model

The code defines the LSTM model using the `LSTM` class. The model architecture consists of an LSTM layer followed by a linear layer (fully connected layer). The model is trained using the training data (`X_train_tensor` and `y_train_tensor`) for a specified number of epochs. The mean squared error (MSE) loss function and the Adam optimizer are used.

### Step 7: Evaluate the Trained Model

After training, the model is evaluated on the test data (`X_test_tensor`). The model predictions (`y_pred_tensor`) are obtained using the trained model and are stored for further analysis.

---

Please note that this summary provides a high-level overview of the code and its functionalities. It is advised to refer to the specific sections of the code for more detailed information and implementation details.
