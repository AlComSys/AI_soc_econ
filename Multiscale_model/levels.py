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

from dataclasses import dataclass, field
import numpy as np



# ------------------------------------------------------------
# 1. Параметры модели
# ------------------------------------------------------------

@dataclass
class ModelParams:
    # Веса социальных и этических издержек
    lambda_S: float = 0.5
    lambda_E: float = 0.5

    # Человек: занятость
    a_aug: float = 0.10      # влияние дополнения труда на занятость
    a_sub: float = 0.30      # влияние замещения труда на занятость
    a_skill: float = 0.20    # влияние AI-навыков на занятость

    # Человек: социальные веса
    b_unemployment: float = 0.5
    b_inequality: float = 0.3
    b_access_gap: float = 0.2
    b_trust_loss: float = 0.2

    # Человек: этические веса
    g_privacy: float = 0.4
    g_bias: float = 0.4
    g_manipulation: float = 0.3
    g_autonomy: float = 0.3

    # Базовые индивидуальные затраты на доступ к ИИ
    person_ai_cost: float = 20_000.0

    # Регион: производственная функция
    theta_AI: float = 0.30
    theta_TR: float = 0.20
    theta_risk: float = 0.20

    # Регион: норма выбытия AI-капитала
    delta_AI: float = 0.15


# ------------------------------------------------------------
# 2. Уровень «человек»
# ------------------------------------------------------------

@dataclass
class Person:
    person_id: str
    region_id: str

    # Труд и доход
    base_task_time: float = 1.0       # часов на задачу без ИИ
    ai_task_time: float = 0.7         # часов на задачу с ИИ
    hourly_wage: float = 800.0        # ставка с накладными расходами
    annual_tasks: float = 1800.0      # задач в год

    # Дополнительный доход от качества работы / продаж
    base_conversion: float = 0.05
    ai_conversion: float = 0.06
    leads: float = 500.0
    average_check: float = 5000.0

    # Занятость
    substitution_rate: float = 0.20   # доля замещаемых задач
    augmentation_rate: float = 0.60   # доля дополняемых задач
    ai_skill_level: float = 0.50      # 0..1
    base_employment_prob: float = 0.95
    unemployment_income: float = 0.0

    # Этика и приватность
    sensitive_data_share: float = 0.30
    consent_quality: float = 0.70     # 0..1
    algorithmic_bias: float = 0.05
    manipulation_risk: float = 0.20
    autonomy_loss: float = 0.20

    def evaluate(self, p: ModelParams) -> dict:
        # Экономия времени
        benefit_time = (
            (self.base_task_time - self.ai_task_time)
            * self.hourly_wage
            * self.annual_tasks
        )

        # Дополнительный доход от качества / конверсии
        benefit_quality = (
            (self.ai_conversion - self.base_conversion)
            * self.leads
            * self.average_check
        )

        benefit = benefit_time + benefit_quality

        # Вероятность сохранения занятости
        employment_prob = (
            self.base_employment_prob
            + p.a_aug * self.augmentation_rate
            - p.a_sub * self.substitution_rate
            + p.a_skill * self.ai_skill_level
        )
        employment_prob = float(np.clip(employment_prob, 0.0, 1.0))

        expected_income = (
            employment_prob * self.hourly_wage
            + (1 - employment_prob) * self.unemployment_income
        )

        # Социальный ущерб
        social_damage = (
            p.b_unemployment * (1 - employment_prob)
            + p.b_inequality * self.algorithmic_bias
            + p.b_access_gap * (1 - self.consent_quality)
            + p.b_trust_loss * self.manipulation_risk
        )

        # Этический ущерб
        privacy_risk = (
            self.sensitive_data_share
            * (1 - self.consent_quality)
        )

        ethical_damage = (
            p.g_privacy * privacy_risk
            + p.g_bias * self.algorithmic_bias
            + p.g_manipulation * self.manipulation_risk
            + p.g_autonomy * self.autonomy_loss
        )

        net_effect = (
            benefit
            - p.person_ai_cost
            - p.lambda_S * social_damage
            - p.lambda_E * ethical_damage
        )

        return {
            "level": "person",
            "id": self.person_id,
            "region_id": self.region_id,
            "benefit": benefit,
            "cost": p.person_ai_cost,
            "social_damage": social_damage,
            "ethical_damage": ethical_damage,
            "net_effect": net_effect,
            "employment_prob": employment_prob,
            "expected_income": expected_income,
        }


# ------------------------------------------------------------
# 3. Уровень «компания»
# ------------------------------------------------------------

@dataclass
class Firm:
    firm_id: str
    region_id: str

    # Доходные механизмы
    base_revenue: float = 100_000_000.0
    conversion_gain: float = 0.01
    leads: float = 20_000.0
    average_check: float = 8_000.0

    # Автоматизация и операционная экономия
    opex_saving: float = 5_000_000.0
    ai_adoption: float = 0.60          # 0..1

    # Предотвращение убытков
    base_failure_prob: float = 0.05
    ai_failure_prob: float = 0.02
    loss_per_event: float = 1_000_000.0

    # Ускорение бизнес-процессов
    cycle_time_saving_months: float = 2.0
    monthly_product_margin: float = 2_000_000.0

    # Стоимость ИИ
    number_of_tasks: float = 100_000.0
    attempt_cost: float = 0.02         # стоимость одной попытки
    retries: float = 1.15
    human_check_share: float = 0.05
    human_check_cost: float = 50.0
    accepted_quality_share: float = 0.95
    error_cost: float = 500.0
    fixed_ai_cost: float = 2_000_000.0

    def evaluate(self, p: ModelParams) -> dict:
        # 1. Рост выручки
        revenue_gain = (
            self.conversion_gain
            * self.leads
            * self.average_check
        )

        # 2. Снижение операционных затрат
        cost_saving = self.opex_saving

        # 3. Предотвращённые убытки
        risk_avoided = (
            (self.base_failure_prob - self.ai_failure_prob)
            * self.loss_per_event
        )

        # 4. Стоимость ускорения
        time_value = (
            self.cycle_time_saving_months
            * self.monthly_product_margin
        )

        gross_benefit = (
            revenue_gain
            + cost_saving
            + risk_avoided
            + time_value
        ) * self.ai_adoption

        # Стоимость ИИ
        variable_cost = (
            self.attempt_cost * self.retries
            + self.human_check_share * self.human_check_cost
            + self.error_cost * (1 - self.accepted_quality_share)
        ) / self.accepted_quality_share

        ai_cost = (
            self.number_of_tasks * variable_cost
            + self.fixed_ai_cost
        )

        # Социальный ущерб компании:
        # необходимость ручного контроля, ошибочные решения,
        # зависимость от внешних платформ.
        social_damage = (
            0.5 * self.human_check_share
            + 0.3 * self.error_cost / 1_000_000
            + 0.2 * (1 - self.accepted_quality_share)
        )

        # Этический ущерб компании
        ethical_damage = (
            0.4 * self.error_cost / 1_000_000
            + 0.4 * (1 - self.accepted_quality_share)
            + 0.2 * (1 - self.ai_adoption)
        )

        net_effect = (
            gross_benefit
            - ai_cost
            - p.lambda_S * social_damage
            - p.lambda_E * ethical_damage
        )

        return {
            "level": "firm",
            "id": self.firm_id,
            "region_id": self.region_id,
            "benefit": gross_benefit,
            "cost": ai_cost,
            "social_damage": social_damage,
            "ethical_damage": ethical_damage,
            "net_effect": net_effect,
        }

    def npv(self, p: ModelParams, years: int = 3, wacc: float = 0.15) -> float:
        """NPV внедрения ИИ с постоянным годовым эффектом."""
        result = self.evaluate(p)
        annual_net_cash_flow = result["net_effect"]
        npv = -self.fixed_ai_cost

        for t in range(1, years + 1):
            npv += annual_net_cash_flow / ((1 + wacc) ** t)

        return npv


# ------------------------------------------------------------
# 4. Уровень «регион»
# ------------------------------------------------------------

@dataclass
class Region:
    region_id: str

    # Отраслевая структура ВРП
    sector_shares: dict = field(default_factory=lambda: {
        "industry": 0.30,
        "services": 0.40,
        "public": 0.30,
    })

    # Отраслевая восприимчивость к ИИ
    sector_ai_intensity: dict = field(default_factory=lambda: {
        "industry": 0.50,
        "services": 0.80,
        "public": 0.40,
    })

    # Технологическая готовность
    infrastructure_index: float = 0.70
    rnd_index: float = 0.60
    innovation_index: float = 0.65
    human_capital_index: float = 0.60
    resilience_index: float = 0.70

    # Производственная функция
    capital: float = 100.0
    labor: float = 1.0
    human_capital: float = 1.0
    alpha: float = 0.35
    beta: float = 0.45
    base_productivity: float = 1.0

    # AI-капитал
    initial_ai_capital: float = 1.0
    annual_ai_investment: float = 0.20

    # Социальные индикаторы
    digital_gap: float = 0.20
    gini_coefficient: float = 0.35

    def technology_readiness(self) -> float:
        return np.mean([
            self.infrastructure_index,
            self.rnd_index,
            self.innovation_index,
            self.human_capital_index,
            self.resilience_index,
        ])

    def ai_intensity(self) -> float:
        return sum(
            share * self.sector_ai_intensity[sector]
            for sector, share in self.sector_shares.items()
        )

    def ai_capital_next_period(self, p: ModelParams) -> float:
        return (
            (1 - p.delta_AI) * self.initial_ai_capital
            + self.annual_ai_investment
        )

    def evaluate(
        self,
        people_results: list[dict],
        firm_results: list[dict],
        p: ModelParams,
    ) -> dict:
        ai_intensity = self.ai_intensity()
        tech_readiness = self.technology_readiness()
        ai_capital = self.ai_capital_next_period(p)

        # Эффективный технологический уровень
        productivity_factor = (
            self.base_productivity
            * (1 + p.theta_AI * ai_intensity)
            * (1 + p.theta_TR * tech_readiness)
            * (1 - p.theta_risk * self.digital_gap)
        )

        # Производственная функция региона
        output = (
            productivity_factor
            * self.capital ** self.alpha
            * self.labor ** self.beta
            * self.human_capital ** (1 - self.alpha - self.beta)
        )

        labor_productivity = output / self.labor

        # Агрегированные выгоды и затраты
        people_benefit = sum(x["benefit"] for x in people_results)
        firm_benefit = sum(x["benefit"] for x in firm_results)

        people_cost = sum(x["cost"] for x in people_results)
        firm_cost = sum(x["cost"] for x in firm_results)
        regional_infrastructure_cost = self.annual_ai_investment * 10_000_000

        total_benefit = people_benefit + firm_benefit
        total_cost = (
            people_cost
            + firm_cost
            + regional_infrastructure_cost
        )

        # Социальный ущерб региона
        person_social = np.mean(
            [x["social_damage"] for x in people_results]
        ) if people_results else 0.0

        social_damage = (
            person_social
            + p.b_inequality * self.gini_coefficient
            + p.b_access_gap * self.digital_gap
        )

        # Этический ущерб региона
        person_ethical = np.mean(
            [x["ethical_damage"] for x in people_results]
        ) if people_results else 0.0

        ethical_damage = (
            person_ethical
            + p.g_bias * self.gini_coefficient
            + p.g_autonomy * (1 - tech_readiness)
        )

        net_effect = (
            total_benefit
            - total_cost
            - p.lambda_S * social_damage
            - p.lambda_E * ethical_damage
        )

        return {
            "level": "region",
            "id": self.region_id,
            "region_id": self.region_id,
            "ai_intensity": ai_intensity,
            "technology_readiness": tech_readiness,
            "ai_capital": ai_capital,
            "productivity_factor": productivity_factor,
            "regional_output": output,
            "labor_productivity": labor_productivity,
            "benefit": total_benefit,
            "cost": total_cost,
            "social_damage": social_damage,
            "ethical_damage": ethical_damage,
            "net_effect": net_effect,
        }


