# AI_soc_econ
Компактная **многомасштабная модель воздействия ИИ на общество и экономику**, построенная на логике раздела 4.2: эффекты ИИ определяются автоматизацией задач, производительностью, скоростью распространения технологии, 
подготовкой кадров и институциональной адаптацией, а негативные эффекты включают цифровое неравенство, вытеснение труда, алгоритмическую дискриминацию, приватность и концентрацию рынков.

## Общая структура

Рассматриваются три связанных уровня:

$$
\text{индивид } i \in \mathcal{I}
\quad \longrightarrow \quad
\text{фирма } f \in \mathcal{F}
\quad \longrightarrow \quad
\text{регион } r \in \mathcal{R}.
$$

Для каждого уровня вводятся:

- \(A_{i,f,r}\) — уровень использования ИИ / автоматизации;
- \(B_{i,f,r}\) — валовая экономическая выгода;
- \(C_{i,f,r}\) — прямые и косвенные издержки ИИ;
- \(S_{i,f,r}\) — социальный ущерб;
- \(E_{i,f,r}\) — этический ущерб;
- \(N_{i,f,r}\) — чистый социально-экономический эффект:

SS
N_{i,f,r}=B_{i,f,r}-C_{i,f,r}-\lambda_S S_{i,f,r}-\lambda_E E_{i,f,r} 
SS,
где $\(\lambda_S,\lambda_E\ge 0\)$ — веса общества/регулятора для социальных и этических издержек. Такая запись соответствует требованию раздела 4.2 оценивать не только финансовую эффективность, 
но и баланс технологической эффективности с социальными издержками. 

## Уровень «люди»

Для работника или пользователя \(i\) эффект ИИ складывается из роста продуктивности, качества услуг и когнитивной разгрузки, но одновременно включает риски вытеснения, неравенства, потери приватности и снижения автономии. [pplxfilegitgateway-projectfiles-prod-use1.s3.us-east-1.amazonaws](https://pplxfilegitgateway-projectfiles-prod-use1.s3.us-east-1.amazonaws.com/projectfiles-prod/gateway-object-store/repos/files-6861b36099cd9ecd83eac8160ffc7bcd/lfs/objects/71/a1/71a122b706cfb16793aaeeaf4acda75fd6904ffa65bb40530fdb4715a1de0387?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Checksum-Mode=ENABLED&X-Amz-Credential=ASIA2F3EMEYEUVGZYP76%2F20261102%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261102T104345Z&X-Amz-Expires=900&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCICMd8X5g%2BTox71waUZffmvB%2BFS6jl%2BiZuOW6bOuBtY4tAiBHrM1PWksT%2F1iypZS%2FQ%2B0BA8NZUQVRv2jM1csYmaJxESqnBQh4EAEaDDY5OTc1MzMwOTcwNSIMqEhfD43%2Bqs56kyqlKoQFMhCznvpFSiOy6yZHPxnTpdFzIEstbOrb%2FjtDhVjsk0HVWPvD1%2BrhIE4PMckGZWAkh%2F7qxBqAFa0KSWkdQDUN5roPx9%2FpOrHyKWdSzQ7SfRMInqlgm5Djha%2BobXnVWYqJZjy3Jf3a3ouz3W77pxGEy2nNEzs6I1pTybex%2ByFPC3RSeGVu0JYDfBTQkCd5NspthJKQmkWeDqJ0UjG8S0gfEEszQ%2FgCcKYatrC85ElS7Nzueaoeqpi7GuzbUNgfxXFajGHImn4V4sB6PG67AgBzT%2Fe79kU4V1D7kpYeEZjddfki1l4Vz7PQ7w5zigF%2FArjlVhALEGKwZObYfdu5u0T%2B8bYsOgl1rMT2EGolXRU7LjTw%2F%2F%2FQvo7W3%2BGQlPt9GBGj6zcZQ1KRcGMmXTBWc8ywbY91N96pVUwmJlGF2IL%2FZuNng9x2PesRXXc1u9GSA6Yzn19ez0wL%2FnboHAQwruMP8Hoh%2F8BR9trLutUyasY%2F03oyXZ6H%2BD3zX5Gc%2FnXoKDsySRddlIGDgZkY%2FLPiXcovpr4mnBiPjDqE9M41fH%2F54mFEaX4LJW2mrMPxK6dy79E0YmkLoPeevmyu2axiBRDX6P2rYt8ZCEbF8ZIX2kfVn3keyJ6e2b9PfuMlChDhDi4ai2lA9FnAHNUz8WXqcJBzz9wGq0lYdyTzcbOICeR7Vdot2vY47AdcvQ1fVK6g6h%2FnN3KWNjUIyQy9YwGkTY%2BgRTJ1%2FPKXq5qrM8YeBq2XomIN08JGAlgCnIRuSvL8a9dJnyvkkIx3T2DxCaR1WgM%2F93OsAvunN7sg2EDcyJ9h6JR%2B0BYKnTKMqKJrCD7nfbfklCUnpYe%2B4tfZp2kq96MQDehwZvQwsuug1wY6kQEdYQeihd9cYEUMLKglVpKdnzblVnql%2Fb8y%2BCLE2y3QqY1PTcxjjy7H8ku3Om%2B11bU86Akbe8L%2BnHuUUJBx3AiuffIh%2FscAHj%2F8lCNnyUQVl2KbTPHigBQaWVzDRajkKJ2kGpHw6EH2OFt30nPlqfeUf%2FgXmX5ma4ozDsIUSrsaW8FkmhXjXOC379isx6FJAtT1&X-Amz-SignedHeaders=host&response-content-type=application%2Fpdf&x-id=GetObject&X-Amz-Signature=4b94d033decf0f11f58abcbe700a9359afc8b191fd6cb7ba9478346ae30ba63a)

### Экономический эффект человека

Пусть:

- \(T_{i0}\) — базовое время выполнения задач;
- \(T_{i1}\) — время с использованием ИИ;
- \(w_i\) — часовая ставка с накладными расходами;
- \(V_i\) — объём задач;
- \(q_i\) — доля качественно выполненных задач;
- \(P_i^{\mathrm{empl}}\) — вероятность сохранения или получения занятости.

Тогда прямой эффект производительности:

$$
\Delta LP_i = \frac{LP_{i1}-LP_{i0}}{LP_{i0}}, \qquad LP_i=\frac{Q_i}{L_i},
$$
где \(Q_i\) — результат труда, \(L_i\) — трудозатраты. 


Экономия времени и труда:

$$
B_i^{\mathrm{time}} = \left(T_{i0}-T_{i1}\right)w_iV_i.
$$

Эта формула соответствует приведённому в разделе 4.2 «эффекту ускорения»: экономия времени превращается в деньги, если высвобожденное время используется продуктивно или позволяет избежать найма. 

Доходный эффект от повышения качества или конверсии:

$$
B_i^{\mathrm{quality}} = \left(CR_{i1}-CR_{i0}\right)N_i^{\mathrm{leads}}\overline{p}_i,
$$

где \(CR_i\) — конверсия, \(N_i^{\mathrm{leads}}\) — число обращений, \(\overline{p}_i\) — средний чек.

Итоговая индивидуальная выгода:

$$
B_i = B_i^{\mathrm{time}}+B_i^{\mathrm{quality}} + \delta_i B_i^{\mathrm{new}},
$$

где \(B_i^{\mathrm{new}}\) — доход от новых задач, продуктов или компетенций, созданных благодаря ИИ, а \(\delta_i\in[0,1]\) — способность человека использовать эти возможности.

### Занятость и неравенство

Коэффициент замещения и дополнения труда:

$$
S_i^{\mathrm{sub}} = \frac{N_{i}^{\mathrm{substituted}}}{N_i^{\mathrm{exposed}}},  \qquad A_i^{\mathrm{aug}} = \frac{N_i^{\mathrm{augmented}}}{N_i^{\mathrm{exposed}}}.
$$

Раздел 4.2 использует именно эти показатели, чтобы различить вытеснение и дополнение труда. 

Вероятность сохранения занятости можно задать как:

$$
P_i^{\mathrm{empl}} = P_{i0}^{\mathrm{empl}}  + \alpha_1 A_i^{\mathrm{aug}} - \alpha_2 S_i^{\mathrm{sub}} + \alpha_3 R_i^{\mathrm{skill}},
$$

где \(R_i^{\mathrm{skill}}\in[0,1]\) — уровень AI-компетенций и переподготовки. Ожидаемый доход:

$$
W_i^{\mathrm{AI}} = P_i^{\mathrm{empl}}w_{i1} + \left(1-P_i^{\mathrm{empl}}\right)w_i^{\mathrm{unemp}}. 
$$

Чистый индивидуальный эффект:

$$
N_i = B_i - C_i^{\mathrm{AI}}  - \lambda_S S_i  - \lambda_E E_i.
$$

### Социальные и этические риски человека

Социальный ущерб:

$$
S_i = \beta_1 U_i^{\mathrm{job}} + \beta_2 G_i^{\mathrm{income}}
+ \beta_3 D_i^{\mathrm{access}}
+ \beta_4 \Delta \mathrm{Trust}_i^-,
$$

где \(U_i^{\mathrm{job}}\) — риск безработицы, \(G_i^{\mathrm{income}}\) — рост неравенства доходов, \(D_i^{\mathrm{access}}\) — цифровой разрыв, \(\Delta \mathrm{Trust}_i^-\) — снижение доверия к цифровым сервисам. 

Этический ущерб:

$$
E_i = \gamma_1 \mathrm{Priv}_i +
\gamma_2 \mathrm{Bias}_i
+
\gamma_3 \mathrm{Manip}_i
+
\gamma_4 \mathrm{Autonomy}_i^-.
$$

Здесь:

$$
\mathrm{Bias}_i = \left| FPR_{i,g_1}-FPR_{i,g_2} \right|  +
\left|
FNR_{i,g_1}-FNR_{i,g_2}
\right|,
$$

— мера алгоритмической дискриминации между защищаемыми группами \(g_1,g_2\); раздел 4.2 предлагает использовать разрывы false positive/false negative rate и demographic parity difference. 

Приватность:

$$
\mathrm{Priv}_i = \frac{D_i^{\mathrm{sensitive}}}{D_i^{\mathrm{total}}} \cdot \left(1-\mathrm{Consent}_i\right),
$$

где \(D_i^{\mathrm{sensitive}}\) — объём чувствительных данных, \(\mathrm{Consent}_i\) — качество информированного согласия и контроля пользователя.

## Уровень «компании»

Для фирмы \(f\) ИИ влияет через снижение затрат, рост выручки, предотвращение убытков и ускорение бизнес-процессов. Раздел 4.2 сводит эти механизмы в валовую выгоду \(GB\). 

### Валовая выгода фирмы

$$
GB_f =
\Delta Revenue_f
+
\Delta CostSave_f
+
\Delta RiskAvoid_f
+
\Delta TimeValue_f.
$$

Компоненты:

$$
\Delta Revenue_f =
\left(CR_{f1}-CR_{f0}\right)N_f^{\mathrm{leads}}\overline{p}_f
+
\Delta Q_f^{\mathrm{AI}},
$$

$$
\Delta CostSave_f =
\sum_{k}
\left(T_{fk0}-T_{fk1}\right)w_{fk}V_{fk}
+
\Delta C_f^{\mathrm{opex}},
$$

$$
\Delta RiskAvoid_f =
\sum_{k}
\left(P_{fk0}^{\mathrm{fail}}-P_{fk1}^{\mathrm{fail}}\right)
C_{fk}^{\mathrm{loss}},
$$

$$
\Delta TimeValue_f =
\sum_{p}
\Delta t_{fp}^{\mathrm{cycle}}
\cdot
m_{fp}^{\mathrm{month}},
$$

где \(m_{fp}^{\mathrm{month}}\) — среднемесячная маржа продукта \(p\), а \(\Delta t_{fp}^{\mathrm{cycle}}\) — сокращение цикла вывода продукта или обслуживания. Эти четыре слагаемых прямо соответствуют классификации позитивной экономики ИИ.

### Затраты на ИИ

Для задачи \(k\):

$$
C_{fk} =
N_{fk}
\cdot
\frac{
c_{fk}^{\mathrm{attempt}}R_{fk}
+
c_{fk}^{\mathrm{human}}h_{fk}
+
c_{fk}^{\mathrm{error}}\left(1-q_{fk}\right)
}
{q_{fk}}
+
C_{fk}^{\mathrm{fix}}.
$$

Здесь:

- \(N_{fk}\) — число задач;
- \(c_{fk}^{\mathrm{attempt}}\) — стоимость одной попытки модели;
- \(R_{fk}\) — среднее число попыток;
- \(h_{fk}\) — доля задач с ручной проверкой;
- \(q_{fk}\) — доля принятых качественных результатов;
- \(c_{fk}^{\mathrm{error}}\) — стоимость ошибочного решения;
- \(C_{fk}^{\mathrm{fix}}\) — фиксированные затраты на разработку, мониторинг и инфраструктуру.

Число повторов зависит от точности модели:

$$
R_{fk} \approx
1+
\frac{1-a_{fk}}{\rho_{fk}}
+
h_{fk},
$$

где \(a_{fk}\) — accuracy, \(\rho_{fk}\) — вероятность исправления ошибки при повторной попытке. 

Стоимость одной принятой задачи:

$$
c_{fk}^{\mathrm{accepted}} =
\frac{
c_{fk}^{\mathrm{attempt}}R_{fk}
+
c_{fk}^{\mathrm{human}}h_{fk}
}
{q_{fk}}.
$$

### Финансовый эффект компании

Чистый денежный поток:

$$
NCF_{ft} = GB_{ft} - C_{ft}^{\mathrm{AI}}  - C_{ft}^{\mathrm{adapt}} - C_{ft}^{\mathrm{risk}}.
$$

NPV проекта:

$$
NPV_f =
\sum_{t=1}^{n} \frac{NCF_{ft}}{(1+\mathrm{WACC}_f)^t} - I_{f0}.
$$

Раздел 4.2 рекомендует использовать горизонт не более трёх лет из-за быстрого устаревания ИИ-технологий и учитывать WACC как ставку дисконтирования. 

ROI:

$$
ROI_f =
\frac{B_f-C_f}{C_f}.
$$

### Производительность и риски фирмы

Общая факторная производительность:

$$
TFP_f =
\frac{Y_f}{K_f^{\alpha}L_f^{\beta}},
$$

где \(Y_f\) — выпуск, \(K_f\) — капитал, \(L_f\) — труд. Рост TFP позволяет отделить реальный эффект ИИ от простого увеличения капитала или численности персонала. 

Риск-поправка фирмы:

$$
R_f^{\mathrm{corp}} =
\omega_1\mathrm{Fail}_f
+
\omega_2\mathrm{Data}_f
+
\omega_3\mathrm{Cyber}_f
+
\omega_4\mathrm{HHI}_f
+
\omega_5\mathrm{Reputation}_f.
$$

Индекс рыночной концентрации:

$$
HHI_f =
\sum_{v}s_{fv}^2,
$$

где \(s_{fv}\) — доля вендора или платформы \(v\) в ИИ-стеке фирмы. Рост HHI отражает зависимость от ограниченного числа поставщиков.

## Уровень «региона»

Регион \(r\) агрегирует эффекты фирм и людей, но добавляет инфраструктурные, институциональные и пространственные факторы. В разделе 4.2 региональный слой связан с технологической готовностью, AI-интенсивностью отраслевой структуры ВРП и производительностью труда. 

### AI-интенсивность региона

Пусть регион состоит из отраслей \(j\), а \(s_{rj}\) — доля отрасли \(j\) в ВРП региона. Тогда структурная AI-интенсивность:

$$
AI_r =
\sum_{j}
s_{rj}AI_j,
$$

где \(AI_j\) — отраслевой индекс восприимчивости к ИИ. Такой подход соответствует расчёту AI-интенсивности региона как взвешенной по структуре ВРП подверженности секторов.

Технологическая готовность:

$$
TR_r =
\frac{1}{5}
\left(
I_r^{\mathrm{infra}}
+
I_r^{\mathrm{R\&D}}
+
I_r^{\mathrm{innov}}
+
I_r^{\mathrm{human}}
+
I_r^{\mathrm{resilience}}
\right).
$$

Раздел 4.2 определяет индекс технологической готовности через пять равновзвешенных блоков: цифровая инфраструктура, наука и исследования, инновационная активность, человеческий капитал и структурная устойчивость. 

### Производственная функция региона

Базовая производственная функция:

$$
Y_r =
A_rK_r^{\alpha}L_r^{\beta}H_r^{1-\alpha-\beta},
$$

где \(H_r\) — человеческий капитал. Влияние ИИ вводится через эффективный технологический уровень:

$$
A_r =
A_{r0}
\left(1+\theta_1 AI_r\right)
\left(1+\theta_2 TR_r\right)
\left(1-\theta_3 R_r^{\mathrm{social}}\right).
$$

Тогда производительность труда:

$$
LP_r =
\frac{Y_r}{L_r}.
$$

Прирост производительности:

$$
\Delta LP_r =
\frac{LP_{r1}-LP_{r0}}{LP_{r0}}.
$$

Раздел 4.2 определяет региональную производительность как отношение реального ВРП к численности рабочей силы. 

### Динамика внедрения ИИ

Траекторию AI-капитала региона можно описать уравнением накопления:

$$
K_r^{\mathrm{AI}}(t+1) = \left(1-\delta_{\mathrm{AI}}\right)K_r^{\mathrm{AI}}(t)  + I_r^{\mathrm{AI}}(t),
$$

где \(\delta_{\mathrm{AI}}\) — норма выбытия ИИ-технологий, \(I_r^{\mathrm{AI}}\) — инвестиции в ИИ. Это соответствует методу непрерывной инвентаризации затрат на сквозные технологии с нормой выбытия, упомянутому в разделе 4.2. 

Уровень внедрения:

$$
A_r(t) = 1-\exp\left[-\kappa_r K_r^{\mathrm{AI}}(t)TR_r(t)\right]
$$

Функция имеет насыщение: при малых инвестициях эффект растёт быстро, а затем ограничивается инфраструктурой, кадрами и институциональной готовностью.

### Региональный экономический эффект

Агрегированная выгода:

$$
B_r =
\sum_{f\in r}B_f
+
\sum_{i\in r}B_i^{\mathrm{ext}}
+
\Delta Tax_r
+
\Delta Export_r.
$$

Затраты:

$$
C_r = \sum_{f\in r}C_f
+
C_r^{\mathrm{infra}}
+
C_r^{\mathrm{education}}
+
C_r^{\mathrm{regulation}}.
$$

Чистый региональный эффект:

$$
N_r =
B_r-C_r-\lambda_S S_r-\lambda_E E_r.
$$

Вклад в ВРП:

$$
\Delta GRP_r = \sum_{j} \Delta VA_{rj} = 
\sum_{j}
\left(VA_{rj,1}-VA_{rj,0}\right).
$$

Используем прирост добавленной стоимости как показатель создания новой стоимости, а не простого перераспределения доходов.

## Социальные и этические риски региона

Социальный ущерб региона:

$$
S_r =
\eta_1 U_r^{\mathrm{struct}}
+
\eta_2 G_r
+
\eta_3 \mathrm{DigitalGap}_r
+
\eta_4 \mathrm{Polarization}_r
+
\eta_5 \mathrm{TrustGap}_r.
$$

Ключевые показатели:

$$
U_r^{\mathrm{struct}} =
\frac{N_r^{\mathrm{displaced}}}{L_r},
$$

$$
\mathrm{DigitalGap}_r =
\frac{LP_r^{\mathrm{leader}}-LP_r^{\mathrm{laggard}}}{LP_r^{\mathrm{leader}}},
$$

$$
\mathrm{AIAdoptionGap}_r =
\max_{r'}\left(AI_{r'}-AI_r,0\right).
$$

Раздел 4.2 выделяет разрыв производительности фирм-лидеров и отстающих, региональный разрыв внедрения ИИ и коэффициент Джини как индикаторы углубления неравенства. 

Этический ущерб региона:

$$
E_r =
\zeta_1\mathrm{Bias}_r
+
\zeta_2(1-\mathrm{Explain}_r)
+
\zeta_3\mathrm{PrivacyIncidents}_r
+
\zeta_4(1-\mathrm{HITL}_r)
+
\zeta_5\mathrm{EthicalEscalations}_r.
$$

Здесь:

$$ 
\mathrm{HITL}_r =
\frac{N_r^{\mathrm{human\text{-}in\text{-}the\text{-}loop}}}{N_r^{\mathrm{AI\ decisions}}},
$$

— доля высокорисковых решений с человеческим контролем. Низкая доля human-in-the-loop и низкая объяснимость решений повышают риск утраты подотчётности. 

## Связь уровней

Модель должна быть согласована снизу вверх и сверху вниз.

### Агрегирование снизу вверх

Региональные переменные формируются из индивидуальных и фирменных:

$$
L_r=\sum_{i\in r}L_i, \qquad
Y_r=\sum_{f\in r}Y_f,
\qquad
B_r=\sum_{f\in r}B_f+\sum_{i\in r}B_i^{\mathrm{ext}},
$$

$$
AI_r =
\sum_j s_{rj}AI_j,
\qquad
S_r=\sum_{i,f\in r}\pi_{i,f}S_{i,f}.
$$

### Обратные связи сверху вниз

Регион влияет на людей и фирмы через доступность инфраструктуры, кадров и регуляторной среды:

$$
A_f =
A_f^0
\cdot
g_1(TR_r)
\cdot
g_2(AI_r)
\cdot
g_3(R_r^{\mathrm{reg}}),
$$

$$
R_i^{\mathrm{skill}} = R_i^{\mathrm{skill},0} + \phi_1 C_r^{\mathrm{education}} - \phi_2 \mathrm{DigitalGap}_r.
$$

Таким образом, недостаток региональной инфраструктуры и переподготовки снижает adoption ИИ на фирмах и увеличивает индивидуальные риски, а рост AI-интенсивности и технологической готовности усиливает положительные эффекты.

## Итоговая система уравнений

Многомасштабную модель можно записать как систему:

$$
\begin{cases}
N_i=B_i-C_i-\lambda_S S_i-\lambda_E E_i,\$$3pt]
N_f=GB_f-C_f^{\mathrm{AI}}-C_f^{\mathrm{adapt}}-C_f^{\mathrm{risk}}-\lambda_S S_f-\lambda_E E_f,\$$3pt]
N_r=B_r-C_r-\lambda_S S_r-\lambda_E E_r,\$$3pt]
GB_f=\Delta Revenue_f+\Delta CostSave_f+\Delta RiskAvoid_f+\Delta TimeValue_f,\$$3pt]
C_f^{\mathrm{AI}}=\sum_k C_{fk},\$$3pt]
Y_r=A_rK_r^{\alpha}L_r^{\beta}H_r^{1-\alpha-\beta},\$$3pt]
A_r=A_{r0}(1+\theta_1AI_r)(1+\theta_2TR_r)(1-\theta_3R_r^{\mathrm{social}}),\$$3pt]
K_r^{\mathrm{AI}}(t+1)=(1-\delta_{\mathrm{AI}})K_r^{\mathrm{AI}}(t)+I_r^{\mathrm{AI}}(t),\$$3pt]
AI_r=\sum_j s_{rj}AI_j,\$$3pt]
TR_r=\frac{1}{5}(I_r^{\mathrm{infra}}+I_r^{\mathrm{R\&D}}+I_r^{\mathrm{innov}}+I_r^{\mathrm{human}}+I_r^{\mathrm{resilience}}).
\end{cases}
$$

## Интерпретация

- **Положительный эффект** возникает, когда \(GB_f\) и \(\Delta GRP_r\) растут быстрее, чем затраты на ИИ, адаптацию персонала и устранение рисков.
- **Нейтральный эффект** возможен, если экономия и рост выручки компенсируются стоимостью ошибок, человеческого контроля, инфраструктуры и переподготовки.
- **Негативный эффект** фиксируется, если:
$$
N_r<0
\quad \text{или} \quad
S_r+E_r > B_r-C_r.
$$

Такая модель позволяет оценивать ИИ не только через NPV и ROI, но и через социально-этическую цену: занятость, неравенство, дискриминацию, приватность, объяснимость, 
доверие и концентрацию рыночной власти. Именно такой баланс заложен в разделе 4.2 как основа оценки внедрения инновационных программных решений. 
