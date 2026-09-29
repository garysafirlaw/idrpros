# Build /es/index.html from /index.html by exact phrase replacement.
# Every English phrase must be found exactly once (or the count given), so
# drift between the two pages fails loudly instead of leaving English behind.
import sys

import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..") + "/"
src = open(ROOT + "index.html", encoding="utf-8").read()

# (english, spanish[, expected_count])
T = [
# ---- head ----
('<html lang="en">', '<html lang="es">'),
('<title>IDR Pros | Out-of-Network Reimbursement Recovery for Florida Providers</title>',
 '<title>IDR Pros | Recuperación de reembolsos fuera de la red para proveedores de la Florida</title>'),
('content="IDR Pros, serviced by Smith Law, recovers underpaid out-of-network claims for Florida physicians and hospital groups through federal IDR and Florida state court. Contingency fee. Complimentary claims review."',
 'content="IDR Pros, con servicios de Smith Law, recupera reclamaciones fuera de la red pagadas de menos para médicos y grupos hospitalarios de la Florida, mediante el IDR federal y los tribunales estatales de la Florida. Honorarios de contingencia. Revisión de reclamaciones sin costo."'),
('<link rel="canonical" href="https://idrpros.com/">',
 '<link rel="canonical" href="https://idrpros.com/es/">\n'
 '<link rel="alternate" hreflang="en" href="https://idrpros.com/">\n'
 '<link rel="alternate" hreflang="es" href="https://idrpros.com/es/">\n'
 '<link rel="alternate" hreflang="x-default" href="https://idrpros.com/">'),
('<meta property="og:title" content="IDR Pros | Maximizing What You\'re Owed">',
 '<meta property="og:title" content="IDR Pros | Maximizamos lo que se le debe">\n<meta property="og:locale" content="es_US">'),
('content="How Florida law recovers what IDR cannot. Out-of-network reimbursement recovery for Florida providers, on contingency."',
 'content="Cómo la ley de la Florida recupera lo que el IDR no puede. Recuperación de reembolsos fuera de la red para proveedores de la Florida, con honorarios de contingencia."'),
('<meta property="og:url" content="https://idrpros.com/">', '<meta property="og:url" content="https://idrpros.com/es/">'),
('"slogan": "Maximizing what you\'re owed",', '"slogan": "Maximizamos lo que se le debe",'),
('"description": "Out-of-network reimbursement recovery for Florida healthcare providers: federal IDR and Florida state court litigation.",',
 '"description": "Recuperación de reembolsos fuera de la red para proveedores de salud de la Florida: IDR federal y litigio en los tribunales estatales de la Florida.",\n  "inLanguage": "es",'),
('"url": "https://idrpros.com/",', '"url": "https://idrpros.com/es/",'),

# ---- header ----
('<a class="skip" href="#main">Skip to content</a>', '<a class="skip" href="#main">Ir al contenido</a>'),
('<a class="brand" href="/" aria-label="IDR Pros, home">', '<a class="brand" href="/es/" aria-label="IDR Pros, inicio">'),
('<span>Serviced by Smith Law</span>', '<span>Con servicios de Smith Law</span>'),
('<a class="head-lang" href="/es/" hreflang="es" lang="es">Español</a>',
 '<a class="head-lang" href="/" hreflang="en" lang="en">English</a>'),
('<span class="cta-long">Claims review</span><span class="cta-short">Review</span>', '<span class="cta-long">Revisión de reclamaciones</span><span class="cta-short">Revisión</span>'),

# ---- hero ----
('alt="IDR Pros: Maximizing what you\'re owed. Serviced by Smith Law."',
 'alt="IDR Pros: Maximizamos lo que se le debe. Con servicios de Smith Law."', 2),
('<div class="eyebrow">Out-of-network reimbursement · Florida</div>', '<div class="eyebrow">Reembolsos fuera de la red · Florida</div>'),
('<h1 id="hero-title">IDR is just the beginning.</h1>', '<h1 id="hero-title">El IDR es solo el comienzo.</h1>'),
('<p class="sub">Florida law recovers what IDR cannot.</p>', '<p class="sub">La ley de la Florida recupera lo que el IDR no puede.</p>'),
('<p class="lede">IDR Pros, serviced by Dan Smith, Esq. of Smith Law, represents Florida physicians, physician groups, and hospital-based departments against Blue Cross, United, Cigna, Aetna, and other carriers. Every underpaid claim is pursued through federal IDR, Florida state court, or both.</p>',
 '<p class="lede">IDR Pros, con servicios de Dan Smith, Esq., de Smith Law, representa a médicos, grupos médicos y departamentos hospitalarios de la Florida frente a Blue Cross, United, Cigna, Aetna y otras aseguradoras. Cada reclamación pagada de menos se persigue mediante el IDR federal, los tribunales estatales de la Florida, o ambos.</p>'),
('<a class="btn btn-red" href="#review">Request a complimentary claims review</a>', '<a class="btn btn-red" href="#review">Solicite una revisión de reclamaciones sin costo</a>'),
('<a class="btn btn-ghost" href="tel:+18135233134">Call (813) 523-3134</a>', '<a class="btn btn-ghost" href="tel:+18135233134">Llame al (813) 523-3134</a>'),
('<p class="byline"><b>Contingency fee.</b> No hourly billing, no retainer, no upfront cost.</p>',
 '<p class="byline"><b>Honorarios de contingencia.</b> Sin cobro por hora, sin anticipo, sin costos iniciales.</p>'),
('<aside class="results-card" aria-label="Recent results">', '<aside class="results-card" aria-label="Resultados recientes">'),
('<header><span>Our results</span><i>IDR + Florida litigation</i></header>', '<header><span>Nuestros resultados</span><i>IDR + litigio en la Florida</i></header>'),
('<div><dt>90%+</dt><dd>IDR win rate</dd></div>', '<div><dt>90%+</dt><dd>Tasa de éxito en IDR</dd></div>'),
('<dd>Recovered in underpaid claims for a single hospital group</dd>', '<dd>Recuperados en reclamaciones pagadas de menos para un solo grupo hospitalario</dd>'),
('<dd>Prior payment levels secured in new in-network agreements</dd>', '<dd>Los niveles de pago anteriores, obtenidos en nuevos contratos dentro de la red</dd>'),
('<div><dt>4 yrs</dt><dd>Lookback on old out-of-network claims</dd></div>', '<div><dt>4 años</dt><dd>Hacia atrás en reclamaciones antiguas fuera de la red</dd></div>'),
('<div class="fine">Past results do not guarantee future outcomes.</div>', '<div class="fine">Los resultados anteriores no garantizan resultados futuros.</div>'),

# ---- system is working ----
('<div class="eyebrow">The No Surprises Act</div>', '<div class="eyebrow">La ley No Surprises Act</div>'),
('<h2 id="system-title">The system is working, for providers who know how to use it.</h2>',
 '<h2 id="system-title">El sistema funciona, para los proveedores que saben usarlo.</h2>'),
('<p>The No Surprises Act gave providers a federal arbitration process to challenge insurer underpayment. Nationally, the numbers favor providers.</p>',
 '<p>La ley federal No Surprises Act dio a los proveedores un proceso de arbitraje federal para impugnar los pagos insuficientes de las aseguradoras. A nivel nacional, las cifras favorecen a los proveedores.</p>'),
('<span>of IDR determinations nationally go to the provider</span>', '<span>de las decisiones de IDR a nivel nacional favorecen al proveedor</span>'),
('<span>average award, measured against the insurer-calculated median in-network rate</span>',
 '<span>laudo promedio, comparado con la tarifa mediana dentro de la red calculada por la aseguradora</span>'),
('<span>disputes filed per month</span>', '<span>disputas presentadas por mes</span>'),
('<span>the volume regulators originally projected</span>', '<span>el volumen que los reguladores proyectaron originalmente</span>'),
('<p><strong>Our results are stronger.</strong> Our IDR win rate exceeds 90%. We have recovered multiples of Medicare rates for specialties from hospitalist groups to trauma surgeons. And when we use litigation outcomes to negotiate in-network agreements, we have secured rates three times previous payment levels.</p>',
 '<p><strong>Nuestros resultados son mejores.</strong> Nuestra tasa de éxito en IDR supera el 90%. Hemos recuperado múltiplos de las tarifas de Medicare para especialidades que van desde grupos de hospitalistas hasta cirujanos de trauma. Y cuando usamos los resultados de litigio para negociar contratos dentro de la red, hemos obtenido tarifas tres veces mayores que los niveles de pago anteriores.</p>'),
('<p class="kicker">But IDR is only half the story. The real story is Florida.</p>',
 '<p class="kicker">Pero el IDR es solo la mitad de la historia. La verdadera historia es la Florida.</p>'),

# ---- two prongs ----
('<div class="eyebrow">Two prongs</div>', '<div class="eyebrow">Dos vías</div>'),
('<h2 id="prongs-title">Every claim gets pursued.</h2>', '<h2 id="prongs-title">Cada reclamación se persigue.</h2>'),
('<p>Our software connects to the billing system you already use and sorts every underpaid claim into the forum where it recovers the most.</p>',
 '<p>Nuestro software se conecta con el sistema de facturación que usted ya usa y clasifica cada reclamación pagada de menos hacia el foro donde más se recupera.</p>'),
('<div class="flow-src">Your underpaid out-of-network claims</div>', '<div class="flow-src">Sus reclamaciones fuera de la red pagadas de menos</div>'),
('<div class="tag">Prong 1</div>', '<div class="tag">Vía 1</div>'),
('<h3>Federal IDR for eligible claims</h3>', '<h3>IDR federal para las reclamaciones elegibles</h3>'),
('<p>Our proprietary software integrates directly with your current billing system to identify which claims are IDR-eligible. Our team prepares submissions calibrated to win.</p>',
 '<p>Nuestro software propio se integra directamente con su sistema de facturación actual para identificar qué reclamaciones son elegibles para IDR. Nuestro equipo prepara presentaciones diseñadas para ganar.</p>'),
('<li>Eligibility identified automatically from your billing data</li>', '<li>Elegibilidad identificada automáticamente a partir de sus datos de facturación</li>'),
('<li>Submissions prepared by our team</li>', '<li>Presentaciones preparadas por nuestro equipo</li>'),
('<li>Unpaid awards enforced through Florida civil litigation, not CMS complaints</li>',
 '<li>Laudos impagos ejecutados mediante litigio civil en la Florida, no con quejas ante CMS</li>'),
('<div class="tag">Prong 2</div>', '<div class="tag">Vía 2</div>'),
('<h3>Florida litigation for everything else</h3>', '<h3>Litigio en la Florida para todo lo demás</h3>'),
('<p>The same software identifies which claims are eligible for Florida state court action and appeal.</p>',
 '<p>El mismo software identifica qué reclamaciones son elegibles para acción y apelación en los tribunales estatales de la Florida.</p>'),
("<li>The 17–20% of disputes found ineligible for IDR nationally, recovered through direct lawsuits under Florida's statutory framework</li>",
 '<li>El 17–20% de las disputas declaradas no elegibles para IDR a nivel nacional, recuperadas mediante demandas directas bajo el marco legal de la Florida</li>'),
('<li>Underpaid out-of-network claims that were never IDR-eligible, recovered too</li>',
 '<li>Las reclamaciones fuera de la red pagadas de menos que nunca fueron elegibles para IDR, también recuperadas</li>'),
('<b>4 years</b>', '<b>4 años</b>'),
('<p><strong>No claim falls through the cracks.</strong> We can go back four years on old out-of-network claims, so revenue you may have written off is still recoverable.</p>',
 '<p><strong>Ninguna reclamación se queda en el camino.</strong> Podemos remontarnos cuatro años en reclamaciones antiguas fuera de la red, así que los ingresos que usted quizás dio por perdidos todavía se pueden recuperar.</p>'),

# ---- Florida law ----
('<div class="eyebrow">Florida law</div>', '<div class="eyebrow">La ley de la Florida</div>'),
('<h2 id="fl-title">Why Blue Cross, United, Cigna, and Aetna settle.</h2>', '<h2 id="fl-title">Por qué Blue Cross, United, Cigna y Aetna llegan a acuerdos.</h2>'),
('<p>Long before Congress passed the No Surprises Act, Florida enacted statutes creating independent, enforceable rights for nonparticipating providers. In January 2022, CMS formally recognized those laws as "specified state laws" that control over the federal default.</p>',
 '<p>Mucho antes de que el Congreso aprobara la No Surprises Act, la Florida promulgó leyes que crean derechos independientes y exigibles para los proveedores no participantes. En enero de 2022, CMS reconoció formalmente esas leyes como "leyes estatales especificadas" (<i lang="en">specified state laws</i>) que prevalecen sobre la norma federal supletoria.</p>'),
("<h3>Florida's reimbursement standard favors providers.</h3>", '<h3>El estándar de reembolso de la Florida favorece a los proveedores.</h3>'),
("<p>Under <span class=\"cite\">Fla. Stat. § 627.64194</span> and <span class=\"cite\">§ 641.513(5)</span>, insurers must reimburse nonparticipating providers at the lesser of the provider's charges, the usual and customary charges for similar services in the community, or a mutually agreed amount. Florida law requires the very factors that support higher reimbursement.</p>",
 '<p>Según <span class="cite">Fla. Stat. § 627.64194</span> y <span class="cite">§ 641.513(5)</span>, las aseguradoras deben reembolsar a los proveedores no participantes la cantidad menor entre los cargos del proveedor, los cargos usuales y acostumbrados por servicios similares en la comunidad, o un monto acordado mutuamente. La ley de la Florida exige precisamente los factores que respaldan un reembolso mayor.</p>'),
('<h3>Providers can sue directly in state court.</h3>', '<h3>Los proveedores pueden demandar directamente en el tribunal estatal.</h3>'),
('<p><span class="cite">Section 627.64194(6)</span> gives providers a choice: resolve disputes through voluntary state arbitration, or go directly to a court of competent jurisdiction. Full discovery. Jury trials. Judicial review. Tools that no arbitration process provides.</p>',
 '<p>La <span class="cite">sección 627.64194(6)</span> da a los proveedores una opción: resolver las disputas mediante arbitraje estatal voluntario o acudir directamente a un tribunal competente. Descubrimiento de pruebas completo. Juicios con jurado. Revisión judicial. Herramientas que ningún proceso de arbitraje ofrece.</p>'),
('<div class="compare-label">Federal IDR compared with Florida law</div>', '<div class="compare-label">IDR federal frente a la ley de la Florida</div>'),
('<th scope="col">Federal IDR</th><th scope="col" class="fl">Florida law</th>', '<th scope="col">IDR federal</th><th scope="col" class="fl">Ley de la Florida</th>'),
('<tr><th scope="row">Payment anchor</th><td>Insurer-calculated QPA</td><td class="fl">Usual and customary charges in the community</td></tr>',
 '<tr><th scope="row">Base del pago</th><td>QPA calculado por la aseguradora</td><td class="fl">Cargos usuales y acostumbrados en la comunidad</td></tr>'),
('<tr><th scope="row">Billed charges</th><td>Consideration prohibited</td><td class="fl">Part of the statutory standard</td></tr>',
 '<tr><th scope="row">Cargos facturados</th><td>Prohibido considerarlos</td><td class="fl">Parte del estándar legal</td></tr>'),
("<tr><th scope=\"row\">Forum</th><td>Arbitration</td><td class=\"fl\">Arbitration or state court, provider's choice</td></tr>",
 '<tr><th scope="row">Foro</th><td>Arbitraje</td><td class="fl">Arbitraje o tribunal estatal, a elección del proveedor</td></tr>'),
('<tr><th scope="row">Discovery</th><td>None</td><td class="fl">Full discovery</td></tr>',
 '<tr><th scope="row">Descubrimiento de pruebas</th><td>Ninguno</td><td class="fl">Completo</td></tr>'),
('<tr><th scope="row">Jury trial</th><td>No</td><td class="fl">Yes</td></tr>',
 '<tr><th scope="row">Juicio con jurado</th><td>No</td><td class="fl">Sí</td></tr>'),
('<tr><th scope="row">Review</th><td>Very limited</td><td class="fl">Judicial review and appeal</td></tr>',
 '<tr><th scope="row">Revisión</th><td>Muy limitada</td><td class="fl">Revisión judicial y apelación</td></tr>'),
('<p><strong>We have litigated hundreds of lawsuits across thousands of claims against major carriers in Florida, all resolved by settlement or plaintiff judgment.</strong>Insurers settle because a 90%+ IDR win rate, provider-favorable state reimbursement standards, direct court access, and a firm that will litigate to conclusion make settlement the rational choice.</p>',
 '<p><strong>Hemos litigado cientos de demandas, con miles de reclamaciones, contra las principales aseguradoras en la Florida, todas resueltas mediante acuerdo o sentencia a favor del demandante.</strong>Las aseguradoras llegan a acuerdos porque una tasa de éxito en IDR de más del 90%, estándares estatales de reembolso favorables al proveedor, acceso directo a los tribunales y una firma dispuesta a litigar hasta el final hacen del acuerdo la decisión racional.</p>'),
('<div class="carrier-row" aria-label="Carriers litigated against">', '<div class="carrier-row" aria-label="Aseguradoras demandadas">'),
('<span>Other major carriers</span>', '<span>Otras aseguradoras principales</span>'),

# ---- ERISA ----
('<div class="eyebrow">ERISA preemption</div>', '<div class="eyebrow">Preferencia de ERISA</div>'),
('<h2 id="erisa-title">For many providers, ERISA is where claims go to die. <span style="color:var(--red)">Not here.</span></h2>',
 '<h2 id="erisa-title">Para muchos proveedores, ERISA es donde las reclamaciones van a morir. <span style="color:var(--red)">Aquí no.</span></h2>'),
('<p style="margin-top:20px">Insurers have used ERISA preemption as a shield for decades. We have obtained hundreds of provider-friendly court orders defeating the ERISA preemption defense raised by insurance giants, at both the federal and state level, in an unbroken chain dating back to 2017.</p>',
 '<p style="margin-top:20px">Durante décadas, las aseguradoras han usado la preferencia de ERISA (<i lang="en">ERISA preemption</i>) como escudo. Hemos obtenido cientos de órdenes judiciales favorables a los proveedores que derrotan la defensa de preferencia de ERISA planteada por las grandes aseguradoras, tanto a nivel federal como estatal, en una cadena ininterrumpida desde 2017.</p>'),
("<blockquote>If you've been told ERISA means you can't recover, <b>you were told wrong.</b></blockquote>",
 '<blockquote>Si le dijeron que por ERISA no puede recuperar, <b>le dijeron mal.</b></blockquote>'),
('<span>of provider-friendly court orders defeating ERISA preemption</span>', '<span>órdenes judiciales favorables a los proveedores que derrotan la preferencia de ERISA</span>'),
('<b>100s</b>', '<b>Cientos</b>'),
('<span>losses on the ERISA preemption defense</span>', '<span>derrotas frente a la defensa de preferencia de ERISA</span>'),
('<span>unbroken chain of orders, federal and state</span>', '<span>cadena ininterrumpida de órdenes, federales y estatales</span>'),
('<p class="disclaim">Past results do not guarantee future outcomes. Each case is evaluated on its own merits.</p>',
 '<p class="disclaim">Los resultados anteriores no garantizan resultados futuros. Cada caso se evalúa según sus propios méritos.</p>'),

# ---- who + fee ----
('<div class="eyebrow">Who we represent</div>', '<div class="eyebrow">A quién representamos</div>'),
('<h2 id="who-title">If you provide out-of-network care in Florida, we recover the full reimbursement the law provides.</h2>',
 '<h2 id="who-title">Si usted presta atención fuera de la red en la Florida, recuperamos el reembolso completo que la ley establece.</h2>'),
('<p>Solo practitioners, physician groups, and hospital-based departments.</p>', '<p>Médicos independientes, grupos médicos y departamentos hospitalarios.</p>'),
('<h3>Specialties</h3>', '<h3>Especialidades</h3>'),
('<span>Emergency medicine</span>', '<span>Medicina de emergencia</span>'),
('<span>Anesthesiology</span>', '<span>Anestesiología</span>'),
('<span>Surgery</span>', '<span>Cirugía</span>'),
('<span>Hospitalists</span>', '<span>Hospitalistas</span>'),
('<span>Radiology</span>', '<span>Radiología</span>'),
('<span>Groups treating ER-admitted patients</span>', '<span>Grupos que atienden a pacientes ingresados por emergencias</span>'),
('<h3>Contingency: you pay nothing unless we recover.</h3>', '<h3>Contingencia: usted no paga nada a menos que recuperemos.</h3>'),
('<b>Hourly billing</b>', '<b>Cobro por hora</b>'),
('<b>Retainer</b>', '<b>Anticipo</b>'),
('<b>Upfront cost</b>', '<b>Costo inicial</b>'),
('<p class="fee-line">We get paid when you get paid.</p>', '<p class="fee-line">Nosotros cobramos cuando usted cobra.</p>'),

# ---- contact ----
('<div class="eyebrow">Complimentary claims review</div>', '<div class="eyebrow">Revisión de reclamaciones sin costo</div>'),
('>Act while the landscape favors providers.</h2>', '>Actúe mientras el panorama favorece a los proveedores.</h2>'),
('>The current landscape is extraordinarily favorable for providers, but regulatory pressure is mounting. Providers who act now recover significant revenue. Providers who wait may face a more restrictive process.</p>',
 '>El panorama actual es extraordinariamente favorable para los proveedores, pero la presión regulatoria va en aumento. Los proveedores que actúan ahora recuperan ingresos significativos. Los que esperan pueden enfrentar un proceso más restrictivo.</p>'),
('<small>Call</small>', '<small>Llamar</small>'),
('?subject=Claims%20review%20request"', '?subject=Solicitud%20de%20revisi%C3%B3n%20de%20reclamaciones"'),
('<small>Email</small>', '<small>Correo</small>'),
('<p class="person"><b>Dan Smith, Esq.</b>Smith Law<br>Tampa, Florida</p>', '<p class="person"><b>Dan Smith, Esq.</b>Smith Law<br>Tampa, Florida</p>'),

# ---- form ----
('<form class="intake" name="claims-review" method="POST" action="/thanks/"',
 '<form class="intake" name="claims-review-es" method="POST" action="/es/gracias/"'),
('<input type="hidden" name="form-name" value="claims-review">', '<input type="hidden" name="form-name" value="claims-review-es">'),
('<label>Leave this empty <input', '<label>Deje esto en blanco <input'),
('<h3>Request a claims review</h3>', '<h3>Solicite una revisión de reclamaciones</h3>'),
('<p>Tell us about your practice. Dan will follow up to arrange a review of your claims data.</p>',
 '<p>Cuéntenos sobre su práctica. Dan se comunicará con usted para coordinar una revisión de sus datos de reclamaciones.</p>'),
('<label for="f-name">Your name</label>', '<label for="f-name">Su nombre</label>'),
('<label for="f-title">Title <i>(optional)</i></label>', '<label for="f-title">Cargo <i>(opcional)</i></label>'),
('placeholder="e.g. CFO, Practice Manager"', 'placeholder="p. ej., CFO, gerente"'),
('<label for="f-org">Practice or organization</label>', '<label for="f-org">Práctica u organización</label>'),
('<label for="f-email">Email</label>', '<label for="f-email">Correo electrónico</label>'),
('<label for="f-phone">Phone</label>', '<label for="f-phone">Teléfono</label>'),
('<label for="f-spec">Specialty</label>', '<label for="f-spec">Especialidad</label>'),
('<option value="">Select…</option>', '<option value="">Seleccione…</option>'),
# option labels in Spanish, submitted values stay English so Dan's lead emails read the same
('<option>Emergency medicine</option>', '<option value="Emergency medicine">Medicina de emergencia</option>'),
('<option>Anesthesiology</option>', '<option value="Anesthesiology">Anestesiología</option>'),
('<option>Surgery</option>', '<option value="Surgery">Cirugía</option>'),
('<option>Hospitalist</option>', '<option value="Hospitalist">Hospitalista</option>'),
('<option>Radiology</option>', '<option value="Radiology">Radiología</option>'),
('<option>Hospital or health system</option>', '<option value="Hospital or health system">Hospital o sistema de salud</option>'),
('<option>Multi-specialty group</option>', '<option value="Multi-specialty group">Grupo multiespecialidad</option>'),
('<option>Other</option>', '<option value="Other">Otra</option>'),
('<label for="f-vol">Out-of-network claims per month</label>', '<label for="f-vol">Reclamaciones fuera de la red por mes</label>'),
('<option value="">Not sure</option>', '<option value="">No estoy seguro</option>'),
('<option>Under 100</option>', '<option value="Under 100">Menos de 100</option>'),
('<option>100–500</option>', '<option value="100–500">100–500</option>'),
('<option>500–2,000</option>', '<option value="500–2,000">500–2,000</option>'),
('<option>Over 2,000</option>', '<option value="Over 2,000">Más de 2,000</option>'),
('<label for="f-msg">Anything we should know? <i>(optional)</i></label>', '<label for="f-msg">¿Algo que debamos saber? <i>(opcional)</i></label>'),
('placeholder="Carriers you see most, billing system, IDR experience so far"',
 'placeholder="Aseguradoras más frecuentes, sistema de facturación, experiencia con IDR hasta ahora"'),
('<b>No patient information.</b><span>Please do not include patient names, dates of service, or any other protected health information. Claims data is exchanged securely after we speak.</span>',
 '<b>Sin información de pacientes.</b><span>No incluya nombres de pacientes, fechas de servicio ni ninguna otra información de salud protegida. Los datos de reclamaciones se intercambian de forma segura después de hablar con nosotros.</span>'),
('<button class="btn btn-red" type="submit">Request my claims review</button>', '<button class="btn btn-red" type="submit">Solicitar mi revisión de reclamaciones</button>'),
('<p class="form-note">Submitting this form does not create an attorney-client relationship. Do not send confidential information until one has been established.</p>',
 '<p class="form-note">Enviar este formulario no crea una relación abogado-cliente. No envíe información confidencial hasta que se haya establecido una.</p>'),

# ---- footer ----
('<p><b>Attorney advertising.</b> This website is for informational purposes only and is not legal advice. Viewing this site or contacting us does not create an attorney-client relationship. Past results do not guarantee future outcomes; each case is evaluated on its own merits, and results depend on the facts and law of each matter.</p>',
 '<p><b>Publicidad de abogados.</b> Este sitio web tiene fines exclusivamente informativos y no constituye asesoría legal. Visitar este sitio o comunicarse con nosotros no crea una relación abogado-cliente. Los resultados anteriores no garantizan resultados futuros; cada caso se evalúa según sus propios méritos, y los resultados dependen de los hechos y del derecho aplicable a cada asunto.</p>'),
('<p>National IDR figures are drawn from publicly reported federal IDR data. Statutory references are to the Florida Statutes and are summarized, not quoted in full.</p>',
 '<p>Las cifras nacionales de IDR provienen de datos federales de IDR publicados. Las referencias legales corresponden a los Estatutos de la Florida y se presentan resumidas, no citadas en su totalidad.</p>'),
('<p>The hiring of a lawyer is an important decision that should not be based solely upon advertisements. Before you decide, ask us to send you free written information about our qualifications and experience.</p>',
 '<p>La contratación de un abogado es una decisión importante que no debe basarse únicamente en anuncios publicitarios. Antes de decidir, pídanos que le enviemos información escrita gratuita sobre nuestras calificaciones y experiencia.</p>'),
('<p>IDR Pros is a trade name of Smith Law.', '<p>IDR Pros es un nombre comercial de Smith Law.'),

# ---- scripts ----
('button.textContent = "Sending…";', 'button.textContent = "Enviando…";'),
('status.textContent = "Thank you. Your request has been received, and Dan will be in touch shortly.";',
 'status.textContent = "Gracias. Recibimos su solicitud y Dan se comunicará con usted en breve.";'),
('button.textContent = "Request received";', 'button.textContent = "Solicitud recibida";'),
('status.textContent = "Something went wrong sending your request. Please call (813) 523-3134 or email dan@idrpros.com.";',
 'status.textContent = "Hubo un problema al enviar su solicitud. Llame al (813) 523-3134 o escriba a dan@idrpros.com.";'),
('button.textContent = "Request my claims review";', 'button.textContent = "Solicitar mi revisión de reclamaciones";'),
('// Header lockup stays hidden while the large hero logo is in view.', '// Header lockup stays hidden while the large hero logo is in view.'),
]

out = src
bad = []
for row in T:
    en, es = row[0], row[1]
    n = row[2] if len(row) > 2 else 1
    c = out.count(en)
    if c != n:
        bad.append((c, n, en[:90]))
        continue
    out = out.replace(en, es)
if bad:
    for c, n, en in bad:
        print(f"MISMATCH found {c} expected {n}: {en}")
    sys.exit(1)

import os
os.makedirs(ROOT + "es", exist_ok=True)
open(ROOT + "es/index.html", "w", encoding="utf-8").write(out)
print("wrote es/index.html", len(out))
