class get_sigma:

    def __init__(self, ticker) -> None:

        yfin = yf.Ticker(ticker)
        da = yfin.history(period = '3mo')
        self.price_list =  list(da.iloc[:,3])
        self.return_list = []
        self.price = self.price_list[-1]

    def calculation(self):

        for i in range(1, len(self.price_list)):
            a = np.log(((self.price_list[i]-self.price_list[i-1])/self.price_list[i-1] + 1))
            self.return_list.append(a)
        self.return_array = self.return_list
        self.mu = np.mean(self.return_array)
        self.sigma = np.sqrt((1 / (len(self.return_list) - 1)) * np.sum(((self.return_array - self.mu) ** 2)))
        self.mu_year = self.mu * 252
        self.sigma_year = self.sigma * np.sqrt(252)


class BlackScholes:

    def __init__(self, s, e, sigma, r, delta_t, dividend=0):

        self.S = s
        self.E = e
        self.sigma = sigma
        self.r = r
        self.delta_t = delta_t
        self.dividend = dividend
        partial = self.r - self.dividend + (1/2)*self.sigma**2
        self.d1 = (np.log(self.S/self.E)+partial*self.delta_t)/(self.sigma*np.sqrt(self.delta_t))
        self.d2 = self.d1 - self.sigma*np.sqrt(self.delta_t)

    def black_scholes(self):

        Part_E = self.E * np.exp(-self.r * self.delta_t) * stats.norm.cdf(self.d2)
        Part_S = self.S * np.exp(-self.dividend * self.delta_t) * stats.norm.cdf(self.d1)
        self.Call = Part_S - Part_E
        self.Put = self.Call - self.S + self.E * np.exp(-self.r * self.delta_t)



class JumpDiffusion:

    """                 dS(t)
                        ----- = mu*dt + sigma*dW(t) + dJ(t)
                        S(t-)

                        S = Current Stock Price
                        E = Strike
                        T = Time to maturity in years
                        σ = Annual Volatility
                        m = Mean of Jump Size
                        v = Standard Deviation of Jump Size
                        λ = Number of jumps per year (intensity)
                        dW(t) = Weiner Process
                        N(t) = Compound Poisson Process
    """

    def __init__(self, s, e, sigma, r, T, m, v, lamb):

        self.s = s
        self.e = e
        self.sigma = sigma
        self.r = r
        self.T = T
        self.m = m
        self.v = v
        self.lam = lamb

    def JD_Call(self):
        call_price = 0
        for k in range(50):
            r_k = self.r - self.lam * (self.m - 1) + (k * np.log(self.m) ) / self.T
            sigma_k = np.sqrt(self.sigma ** 2 + (k * self.v ** 2) / self.T)
            k_fact = np.math.factorial(k)
            bs = BlackScholes(self.s, self.e, sigma_k, r_k, self.T)
            bs.black_scholes()
            self.bs_call = bs.Call
            call_price += (np.exp(- self.m * self.lam * self.T) * (self.m * self.lam * self.T) ** k / (k_fact)) * self.bs_call
        return call_price

    def JD_Put(self):
        put_price = 0
        for k in range(50):
            r_k = self.r - self.lam * (self.m - 1) + (k * np.log(self.m) ) / self.T
            sigma_k = np.sqrt(self.sigma ** 2 + (k * self.v ** 2) / self.T)
            k_fact = np.math.factorial(k)
            bs = BlackScholes(self.s, self.e, sigma_k, r_k, self.T)
            bs.black_scholes()
            self.bs_put = bs.Put
            put_price += (np.exp(- self.m * self.lam * self.T) * (self.m * self.lam * self.T) ** k / (k_fact)) * self.bs_put
        return put_price
