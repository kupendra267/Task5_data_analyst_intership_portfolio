from src.data_cleaning import load_and_clean_data
from src.kpi_calculation import calculate_kpis
from src.analysis import analyze_data
from src.visualization import plot_charts

def main():
    # Step 1: Load data
    df = load_and_clean_data("data/sales_data.csv")

    # Step 2: KPIs
    kpis = calculate_kpis(df)
    print("\n📊 KPIs:")
    for key, value in kpis.items():
        print(f"{key}: {value}")

    # Step 3: Analysis
    region_sales, category_sales, monthly_sales = analyze_data(df)

    # Step 4: Visualization
    plot_charts(region_sales, category_sales, monthly_sales)

    print("\n✅ Charts saved in outputs/charts/")

if __name__ == "__main__":
    main()