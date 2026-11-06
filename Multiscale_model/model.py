"""
Многомасштабная модель воздействия ИИ на общество и экономику.

Уровни:
1. Люди: производительность, занятость, доход, цифровые и этические риски.
2. Компании: рост выручки, экономия затрат, предотвращение убытков,
   ускорение процессов, стоимость ИИ и риски.
3. Регионы: AI-интенсивность, технологическая готовность, ВРП,
   производительность труда, неравенство и институциональные риски.

Основной критерий:
N = B - C - lambda_S * S - lambda_E * E

где:
B — валовая выгода;
C — затраты;
S — социальный ущерб;
E — этический ущерб;
N — чистый социально-экономический эффект.
"""

#from dataclasses import dataclass, field
#import numpy as np
import pandas as pd

from levels import ModelParams
from build_data import build_regions,  build_firms, build_persons


# ------------------------------------------------------------
# Запуск модели
# ------------------------------------------------------------

def run_model() -> pd.DataFrame:
    params = ModelParams()

    people =  build_persons()

    firms =  build_firms()

    regions = build_regions()
    
    results = []

    for region in regions:
        region_people = [
            person for person in people
            if person.region_id == region.region_id
        ]

        region_firms = [
            firm for firm in firms
            if firm.region_id == region.region_id
        ]

        people_results = [
            person.evaluate(params)
            for person in region_people
        ]

        firm_results = [
            firm.evaluate(params)
            for firm in region_firms
        ]

        region_result = region.evaluate(
            people_results,
            firm_results,
            params,
        )

        results.append(region_result)
        results.extend(people_results)
        results.extend(firm_results)

    df = pd.DataFrame(results)

    # NPV для компаний
    npv_rows = []
    for firm in firms:
        npv_rows.append({
            "firm_id": firm.firm_id,
            "region_id": firm.region_id,
            "NPV_3y": firm.npv(params, years=3, wacc=0.15),
        })

    npv_df = pd.DataFrame(npv_rows)

    print("Результаты модели:")
    print(
        df[
            [
                "level",
                "id",
                "region_id",
                "benefit",
                "cost",
                "social_damage",
                "ethical_damage",
                "net_effect",
            ]
        ]
        .to_string(index=False)
    )

    print("\nNPV ИИ-проектов компаний:")
    print(npv_df.to_string(index=False))

    return df, npv_df


if __name__ == "__main__":
    results_df, npv_df = run_model()
    results_df.to_excel(
        "ai_multiscale_model_results.xlsx",
        index=False
    )
    npv_df.to_csv(
        "ai_firm_npv_results.csv",
        index=False,
        encoding="utf-8-sig",
    )
