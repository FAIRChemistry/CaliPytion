if __name__ == "__main__":
    x_data = np.load("/Users/max/Documents/GitHub/lars-sah/x_data.npy")
    y_data = np.load("/Users/max/Documents/GitHub/lars-sah/y_data.npy")
    # Step 1: Define the parameters for a 3rd-degree polynomial (cubic equation)
    params = []
    params.append(
        Parameter(
            symbol="a",
            init_value=1.0,
            lower_bound=-1e6,
            upper_bound=1e6,
        )
    )
    params.append(
        Parameter(
            symbol="b",
            init_value=-1.0,
            lower_bound=0,
            upper_bound=1e6,
        )
    )

    # Step 2: Define a 3rd-degree polynomial equation
    # Equation: a * Meth + b * Meth**2 + c * Meth + d
    equation = "a * Meth + b"

    # Step 3: Create a Fitter object with the equation and parameters
    model = Fitter(
        equation=equation,
        indep_var="Meth",
        params=params,
    )

    # Step 4: Print the model details
    print("Independent Variable:", model.indep_var)
    print("Equation:", model.equation)
    print("Initial Parameters:", model.lmfit_params)

    # Step 6: Fit the model to the data
    res = model.fit(y_data, x_data, "Meth")

    # Step 7: Print the result of the fitting process
    print("Fitting Results:", res)

    # Step 8: Calculate and print the critical points (maxima/minima)
    print("Critical Points:", model.calculate_critical_points())

    import matplotlib.pyplot as plt
    import numpy as np

    # Assuming the 'model' and 'res' (fit result) are already defined and you have fitted your model

    # Step 1: Generate points for the fitted curve
    x_range = np.linspace(
        min(x_data), max(x_data), 1000
    )  # Fine grid of x values for smooth curve
    y_fitted = model.predict(x_range)  # Predict y values using the fitted model

    # Step 2: Get the critical points (assumes model.calculate_critical_points() returns critical x values)
    critical_points = model.calculate_critical_points()
    # build array of x and y values for the critical points
    critical_y = [model.predict(np.array([cp[0]])) for cp in critical_points]
    critical_x = [cp[0] for cp in critical_points]

    # Calculate the corresponding y values for the critical points using the model

    unknowns = np.array([1, 2, 4.06])

    # Step 3: Plot the fitted curve
    plt.figure(figsize=(8, 6))
    plt.plot(x_range, y_fitted, label="Fitted Polynomial", color="blue", linewidth=2)

    # Step 4: Plot the original data points
    plt.scatter(x_data, y_data, color="red", label="Data Points", zorder=5)

    # Step 5: Plot the critical points
    plt.scatter(
        critical_x,
        critical_y,
        color="green",
        label="Critical Points",
        zorder=10,
        s=100,
        marker="x",
    )

    # Step 6: Add labels and title
    plt.title("Fitted 3rd-Degree Polynomial and Critical Points")
    plt.xlabel("Meth (Independent Variable)")
    plt.ylabel("Dependent Variable")
    plt.legend()

    unknowns = np.array([-0.06, 2, 2.41])

    # Step 8: Calculate the roots of the equation
    print(model.calculate_roots(unknowns, -1, 2, extrapolate=True))

    # Step 7: Show the plot
    plt.show()
