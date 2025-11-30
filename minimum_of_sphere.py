import numpy as np
import matplotlib.pyplot as plt

def sphere_function(x):
    return np.sum(x**2)

def GWO(max_iter, n_wolves, dim, lb, ub):
    wolves = np.random.uniform(lb, ub, (n_wolves, dim))

    alpha = np.zeros(dim)
    beta = np.zeros(dim)
    delta = np.zeros(dim)

    alpha_score = float("inf")
    beta_score = float("inf")
    delta_score = float("inf")

    convergence_curve = []  

    for t in range(max_iter):
        for i in range(n_wolves):
            fitness = sphere_function(wolves[i])

            if fitness < alpha_score:
                delta_score = beta_score
                delta = beta.copy()

                beta_score = alpha_score
                beta = alpha.copy()

                alpha_score = fitness
                alpha = wolves[i].copy()

            elif fitness < beta_score:
                delta_score = beta_score
                delta = beta.copy()

                beta_score = fitness
                beta = wolves[i].copy()

            elif fitness < delta_score:
                delta_score = fitness
                delta = wolves[i].copy()

        a = 2 - t * (2 / max_iter)

        for i in range(n_wolves):
            for j in range(dim):
                r1, r2 = np.random.rand(), np.random.rand()
                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                D_alpha = abs(C1 * alpha[j] - wolves[i][j])
                X1 = alpha[j] - A1 * D_alpha

                r1, r2 = np.random.rand(), np.random.rand()
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                D_beta = abs(C2 * beta[j] - wolves[i][j])
                X2 = beta[j] - A2 * D_beta

                r1, r2 = np.random.rand(), np.random.rand()
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                D_delta = abs(C3 * delta[j] - wolves[i][j])
                X3 = delta[j] - A3 * D_delta

                wolves[i][j] = (X1 + X2 + X3) / 3

            wolves[i] = np.clip(wolves[i], lb, ub)

        convergence_curve.append(alpha_score)
        print(f"Iteration {t+1}/{max_iter}, Best Score: {alpha_score}")

    return alpha_score, alpha, convergence_curve


max_iter = 10
n_wolves = 10
dim = 5
lb, ub = -5, 5

best_score, best_position, convergence_curve = GWO(max_iter, n_wolves, dim, lb, ub)

print("\nBest Score:", best_score)
print("Best Position:", best_position)

plt.plot(convergence_curve)
plt.title("GWO Convergence Curve")
plt.xlabel("Iteration")
plt.ylabel("Best Fitness Value (Alpha Score)")
plt.grid(True)
plt.show()
