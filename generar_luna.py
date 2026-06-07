import json, os

ENTRIES = {}

# Luna conjuncion Mercurio
ENTRIES["luna_conjuncion_mercurio"] = (
    "Cuando la Luna se encuentra en conjunción con Mercurio, el mundo emocional y el mundo mental se fusionan en una sola corriente de conciencia. "
    "Esta persona no solo siente lo que piensa, sino que piensa lo que siente, en un bucle continuo donde las palabras emergen teñidas por el estado anímico "
    "y los sentimientos buscan desesperadamente ser nombrados. La mente funciona como un espejo sensible de las emociones: cada cambio interno se refleja "
    "al instante en el pensamiento, y cada pensamiento despierta una resonancia afectiva inmediata. Existe una necesidad profunda de comunicar lo que se vive "
    "interiormente, de verbalizar el mundo subterráneo de la psique para poder comprenderlo y, al mismo tiempo, para sentirse comprendido por los demás. "
    "Sin embargo, esta fusión entre emoción y pensamiento puede generar una dificultad para distinguir entre lo que se siente y lo que es objetivamente cierto, "
    "pues los juicios suelen estar impregnados por el estado de ánimo del momento. En los momentos de mayor conciencia, esta configuración se convierte en "
    "un instrumento psicológico de enorme precisión: la persona logra articular sus emociones con una claridad poco común, convirtiéndose en una narradora "
    "natural de su propio mundo interno. La comunicación se vuelve entonces un vehículo de sanación, una forma de darle forma a lo amorfo, de nombrar lo "
    "innombrable. El desafío evolutivo consiste en aprender a observar los pensamientos sin identificarse completamente con ellos, creando un espacio de "
    "testigo interno que permita discernir cuándo la emoción nutre al pensamiento y cuándo lo distorsiona. Cuando se alcanza este equilibrio, la persona "
    "descubre que su mente emocional es su mayor talento: una sensibilidad psicológica que le permite leer entre líneas, percibir los estados anímicos "
    "ajenos con precisión casi intuitiva y expresar lo que otros apenas se atreven a sentir."
)

# Luna sextil Mercurio
ENTRIES["luna_sextil_mercurio"] = (
    "El sextil entre la Luna y Mercurio otorga una comunicación naturalmente teñida de sensibilidad emocional, como si las palabras surgieran bañadas "
    "por una corriente subterránea de sentimientos. Esta persona posee una facilidad innata para expresar lo que siente sin que ello le resulte amenazante, "
    "pues existe una cooperación armoniosa entre su mundo afectivo y su capacidad de verbalización. No necesita luchar para encontrar las palabras adecuadas "
    "cuando se trata de describir sus emociones; estas fluyen con una claridad que sorprende incluso a quienes la rodean. La mente se convierte en una aliada "
    "del corazón, organizando en forma de lenguaje aquello que de otro modo permanecería en el reino de lo informe. Esta configuración abre oportunidades "
    "constantes para integrar la inteligencia emocional en la vida cotidiana: en las conversaciones, en la escritura, en la enseñanza y en todas aquellas "
    "actividades donde la comunicación sensible sea valorada. La persona descubre que puede aprender casi cualquier cosa cuando el contenido resuena con "
    "su mundo afectivo, y tiende a buscar conocimientos que tengan un significado emocional profundo. Existe una curiosidad psicológica natural, un interés "
    "genuino por comprender qué motiva a las personas, qué las hace sentir vivas y qué las lastima. El riesgo de este aspecto armónico es que la facilidad "
    "para expresar las emociones puede llevar a una cierta superficialidad si la persona no se toma el tiempo de profundizar realmente en lo que siente. "
    "La invitación del sextil es a utilizar esta habilidad comunicativa no solo para expresar lo evidente, sino para explorar las capas más sutiles de la "
    "psique, convirtiendo la palabra en una herramienta de autoconocimiento y conexión genuina con los demás."
)

# Luna cuadratura Mercurio
ENTRIES["luna_cuadratura_mercurio"] = (
    "La cuadratura entre la Luna y Mercurio instala una tensión constante entre lo que se siente y lo que se piensa, como si el corazón y la mente "
    "hablaran idiomas diferentes y rara vez se pusieran de acuerdo. Esta persona experimenta una lucha interna entre su necesidad de expresar lo que siente "
    "y la tendencia de su mente a analizar, racionalizar o incluso silenciar sus emociones. Cuando la emoción es intensa, las palabras se atascan, se vuelven "
    "torpes o simplemente no llegan, generando una frustración que solo profundiza el malestar. En otras ocasiones, la mente se dispara con pensamientos "
    "ansiosos que alimentan la inseguridad emocional, creando un bucle donde la persona se siente atrapada en sus propias interpretaciones. La infancia "
    "pudo haber estado marcada por una desconexión entre lo que se sentía en el hogar y lo que se podía expresar abiertamente, quizás porque las emociones "
    "eran minimizadas, intelectualizadas o simplemente no tenían espacio para ser nombradas. Como resultado, la persona adulta puede tender a somatizar "
    "sus conflictos emocionales o a refugiarse en la actividad mental como forma de evitar el contacto con sentimientos incómodos. Sin embargo, esta tensión "
    "contiene una fuerza creativa inmensa. Cuando la persona aprende a habitar la incomodidad entre el pensar y el sentir, descubre que puede utilizar su "
    "mente para dar forma a sus emociones sin traicionarlas. La escritura, la terapia, el arte o cualquier forma de expresión estructurada se convierten "
    "en vehículos de integración. El camino de crecimiento implica precisamente eso: crear puentes donde antes había abismos, entrenar a la mente para que "
    "no juzgue las emociones sino que las contenga, y permitir que los sentimientos informen al pensamiento sin dominarlo. Cuando esta integración ocurre, "
    "la persona desarrolla una inteligencia emocional aguda y auténtica, forjada en el fuego de la contradicción interna."
)

# Luna trino Mercurio
ENTRIES["luna_trino_mercurio"] = (
    "El trino entre la Luna y Mercurio establece una corriente fluida y natural entre las aguas de la emoción y los vientos del pensamiento. "
    "Esta persona posee una facilidad innata para comprender sus propios estados emocionales y para expresarlos con palabras que otros pueden entender "
    "y sentir. La comunicación no es un esfuerzo ni una obligación, sino una extensión natural de su ser, como si hablar de lo que siente fuera tan "
    "sencillo como respirar. Existe una sensibilidad psicológica que opera de manera casi inconsciente: capta los matices emocionales de las situaciones, "
    "lee entre líneas lo no dicho y posee una memoria afectiva que le permite recordar no solo los hechos sino también cómo se sintió en cada momento. "
    "Esta configuración favorece especialmente las actividades donde la palabra y la emoción se entrelazan: la poesía, la escritura terapéutica, la "
    "enseñanza, el asesoramiento psicológico y toda forma de comunicación que busque conmover y conectar. La persona aprende con facilidad cuando el "
    "conocimiento está vinculado a una experiencia emocional significativa, y tiende a rodearse de libros, conversaciones y entornos que estimulen "
    "tanto su mente como su corazón. El peligro de tanta fluidez es que la persona puede volverse perezosa en su autoconocimiento, confiando demasiado "
    "en su facilidad natural para expresar emociones sin tomarse el tiempo de examinarlas con profundidad. El trino ofrece el don, pero la sabiduría "
    "exige que la persona no se duerma en los laureles de su talento comunicativo. Cuando se mantiene despierta y consciente, esta configuración se "
    "convierte en un canal de expresión genuina que no solo beneficia a la persona, sino que inspira y conmueve a quienes tienen la fortuna de escucharla."
)

# Luna oposicion Mercurio
ENTRIES["luna_oposicion_mercurio"] = (
    "La oposición entre la Luna y Mercurio crea una polaridad consciente entre la vida emocional y la vida mental, como si la persona oscilara "
    "entre dos mundos que rara vez se encuentran en el mismo plano. En un momento está completamente identificada con sus emociones, sumergida en "
    "un mar de sentimientos que la desbordan y nublan su capacidad de pensar con claridad. Al momento siguiente, se refugia en la racionalidad, "
    "analizando sus experiencias afectivas desde una distancia que las vacía de vida y las convierte en meros datos fríos. Esta oscilación puede "
    "ser agotadora, tanto para ella como para quienes la rodean, pues nunca se sabe con certeza qué versión de la persona va a aparecer. Las relaciones "
    "significativas suelen activar esta polaridad: cuando alguien importante le habla, la persona puede sentirse emocionalmente expuesta y reaccionar "
    "con una defensa mental, o bien puede sentirse tan abrumada por la carga afectiva del intercambio que las palabras le fallen por completo. "
    "La infancia pudo haber estado marcada por una figura materna o un entorno familiar donde la comunicación emocional era inconsistente, quizás "
    "porque se alternaba entre la sobrecarga afectiva y el silencio racional. El trabajo evolutivo de esta oposición consiste en integrar ambos "
    "polos, reconociendo que la mente y el corazón no son enemigos sino dos formas complementarias de conocer la realidad. Cuando la persona logra "
    "mantener la conciencia de ambos simultáneamente, descubre que puede sentir profundamente sin perderse en la emoción, y pensar con claridad "
    "sin desconectarse de su experiencia afectiva. Las relaciones se convierten entonces en el espejo donde esta integración se perfecciona, "
    "y la comunicación se vuelve un puente sagrado entre dos formas de verdad."
)

# Luna conjuncion Venus
ENTRIES["luna_conjuncion_venus"] = (
    "Cuando la Luna se funde con Venus en conjunción, la necesidad emocional de seguridad y el deseo de amor se convierten en una sola cosa, "
    "indistinguibles la una del otro. Esta persona no puede sentirse segura si no se siente amada, ni puede sentirse amada si no experimenta una "
    "profunda sensación de pertenencia emocional. El afecto no es un lujo ni un complemento en su vida, sino una necesidad tan básica como el "
    "alimento o el refugio. Desde la infancia, la calidez emocional del entorno familiar ha quedado grabada en su psique como el modelo de lo que "
    "el amor debe ser: una presencia suave, receptiva, incondicional. Tiende a buscar relaciones que reproduzcan esa calidez inicial, y cuando las "
    "encuentra, se entrega con una entrega total que puede ser tanto su mayor fortaleza como su mayor vulnerabilidad. Posee una sensibilidad estética "
    "muy desarrollada: la belleza, el arte, la música y todo aquello que toque su corazón de manera armónica la hace sentir viva y conectada. "
    "Su hogar suele ser un espacio cuidadosamente decorado, un nido donde la armonía visual y sensorial refleja su mundo interior. En las relaciones, "
    "es generosa, atenta y profundamente empática, pero puede tener dificultades para establecer límites claros, pues decir que no amenaza su necesidad "
    "de ser querida. La sombra de esta conjunción es la tendencia a fusionarse con el otro, a perder la propia identidad en la búsqueda de amor "
    "y aprobación. El camino de crecimiento implica aprender que el amor verdadero comienza en el amor propio, y que la seguridad que busca afuera "
    "debe primero cultivarse adentro. Cuando logra este equilibrio, se convierte en una fuente de amor inagotable, capaz de nutrir a los demás sin "
    "perderse a sí misma, encarnando la sabiduría del corazón que sabe amar sin posesión."
)

# Luna sextil Venus
ENTRIES["luna_sextil_venus"] = (
    "El sextil entre la Luna y Venus otorga una disposición natural hacia la armonía emocional y la expresión afectiva. Esta persona posee una "
    "facilidad innata para crear relaciones cálidas y nutritivas, como si supiera instintivamente cómo hacer sentir bien a los demás. El amor fluye "
    "sin esfuerzo en su vida, no porque todo sea perfecto, sino porque tiene una capacidad genuina para apreciar la belleza de los pequeños momentos "
    "y para valorar a las personas por lo que son. Su hogar tiende a ser un espacio acogedor donde los demás se sienten bienvenidos, y ella misma "
    "disfruta creando ambientes que invitan al descanso emocional y al intercambio afectivo. Existe una sensibilidad estética que se expresa en la "
    "forma en que se viste, en la música que elige, en la comida que prepara: todo en su vida está impregnado de un deseo de belleza y armonía. "
    "Las relaciones de amistad y familiares suelen ser fuente de satisfacción y apoyo mutuo, pues la persona sabe cómo cuidar los vínculos sin "
    "sofocar ni exigir. Esta configuración abre oportunidades para desarrollar talentos artísticos o terapéuticos, ya que la combinación de "
    "sensibilidad emocional y aprecio por la belleza puede canalizarse hacia la creación o la sanación. Sin embargo, el riesgo de tanta armonía "
    "es que la persona evite el conflicto a toda costa, sacrificando sus propias necesidades con tal de mantener la paz. El sextil ofrece la "
    "oportunidad, pero la persona debe elegir activamente utilizarlo para construir relaciones auténticas, no solo cómodas. Cuando lo hace, "
    "su vida afectiva se convierte en un jardín donde el amor y la belleza crecen de manera natural y generosa."
)

# Luna cuadratura Venus
ENTRIES["luna_cuadratura_venus"] = (
    "La cuadratura entre la Luna y Venus revela una tensión profunda entre la necesidad de seguridad emocional y el deseo de amor y armonía. "
    "Esta persona experimenta el afecto como algo esquivo, que nunca termina de satisfacer por completo. Puede sentir que necesita amor para "
    "sentirse segura, pero cuando el amor llega, algo en su interior le impide confiar plenamente en él. La infancia pudo haber estado marcada "
    "por una desconexión entre la madre y la capacidad de expresar afecto de manera saludable: quizás el amor estaba presente pero condicionado, "
    "o tal vez la calidez emocional alternaba con la frialdad, generando una confusión temprana entre el amor y la inseguridad. Como resultado, "
    "la persona adulta puede oscilar entre la necesidad de fusión y el miedo a la intimidad, entre entregarse por completo y retirarse "
    "abruptamente. Existe una tendencia a idealizar las relaciones y a sufrir cuando la realidad no coincide con la fantasía, o bien a "
    "conformarse con menos de lo que merece por miedo a quedarse sola. El dinero y los placeres materiales también pueden ser un área de "
    "conflicto: la persona puede gastar en exceso para llenar un vacío emocional o, por el contrario, privarse del disfrute por sentirse "
    "merecedora de él. La tensión de esta cuadratura es el motor que impulsa a la persona a sanar su relación con el amor propio. Cuando "
    "comienza a cultivar dentro de sí misma la seguridad y el afecto que busca afuera, las relaciones externas se vuelven menos cargadas "
    "y más auténticas. El camino implica reconciliarse con la propia valía y aprender que el amor no es algo que se gana, sino algo que se es."
)

# Luna trino Venus
ENTRIES["luna_trino_venus"] = (
    "El trino entre la Luna y Venus establece una corriente natural de amor, belleza y armonía que atraviesa toda la vida emocional de la persona. "
    "Esta configuración es una de las más dulces del zodíaco, pues otorga una capacidad innata para dar y recibir afecto de manera genuina y "
    "desinteresada. La persona no necesita esforzarse para ser amable, para crear ambientes armoniosos o para conectar con los demás desde el "
    "corazón; todo esto fluye de manera tan natural que a menudo ni siquiera es consciente del don que posee. Desde la infancia, probablemente "
    "experimentó una relación nutritiva con la madre o con las figuras femeninas de su entorno, lo que estableció una base sólida de seguridad "
    "afectiva que la acompañará toda la vida. En las relaciones, es generosa, leal y profundamente sensible a las necesidades del otro, pero "
    "sin perder su propio centro. Posee un talento natural para las artes, la decoración, la música o cualquier expresión que canalice la "
    "belleza, y tiende a rodearse de objetos, personas y experiencias que alimentan su sentido estético. El peligro de esta armonía es que la "
    "persona puede volverse complaciente, evitando las profundidades más oscuras de la vida emocional por miedo a perturbar su paz interior. "
    "El trino ofrece el don de la gracia afectiva, pero la verdadera evolución exige que la persona no se esconda en la comodidad de las "
    "relaciones armoniosas, sino que utilice esa base de seguridad para explorar también las dimensiones más complejas del amor: el perdón, "
    "la pérdida, el compromiso incondicional. Cuando lo hace, su capacidad de amar se vuelve no solo dulce, sino verdaderamente sabia."
)

# Luna oposicion Venus
ENTRIES["luna_oposicion_venus"] = (
    "La oposición entre la Luna y Venus sitúa a la persona en una encrucijada constante entre sus necesidades emocionales profundas y sus "
    "deseos de amor y de relación. Existe una polaridad entre lo que necesita para sentirse segura y lo que anhela en el amor, y estas dos "
    "fuerzas no siempre apuntan en la misma dirección. Puede buscar parejas que le ofrezcan estabilidad emocional pero que no despierten "
    "su pasión, o sentirse atraída por personas que la conmueven pero que no le brindan la seguridad que su Luna necesita. Esta división "
    "interna se proyecta con frecuencia en las relaciones significativas, donde la persona puede experimentar una sensación de insatisfacción "
    "crónica, como si siempre faltara algo. Las figuras materna y femenina en su vida pudieron haber transmitido mensajes contradictorios "
    "sobre el amor: por un lado el deseo de cuidar y ser cuidada, por otro la necesidad de ser independiente y no depender de nadie. "
    "La persona puede sentirse desgarrada entre el deseo de fundirse con el otro y el miedo a perderse a sí misma en esa fusión. "
    "El trabajo de esta oposición es aprender a integrar ambos polos dentro de sí misma, reconociendo que la seguridad emocional y el amor "
    "no son excluyentes sino complementarios. Las relaciones actúan como espejo de esta tensión interna, mostrando todo aquello que la persona "
    "no ha reconciliado en su propia psique. Cuando comienza a cultivar tanto su propia seguridad como su capacidad de amar sin perderse, "
    "descubre que puede mantener relaciones íntimas sin sacrificar su identidad. La oposición se convierte entonces en una fuente de equilibrio "
    "dinámico, donde la persona aprende a navegar entre la necesidad y el deseo con la sabiduría de quien ha integrado sus contradicciones."
)

# Luna conjuncion Marte
ENTRIES["luna_conjuncion_marte"] = (
    "Cuando la Luna y Marte se encuentran en conjunción, las emociones se cargan de la energía combativa y asertiva del dios de la guerra. "
    "Esta persona siente con intensidad, con una fuerza que puede ser avasalladora tanto para ella como para quienes la rodean. Sus reacciones "
    "emocionales son inmediatas, viscerales, y a menudo se expresan a través del cuerpo antes de que la mente tenga tiempo de procesarlas. "
    "La ira no es una emoción más entre otras: es una fuerza primaria que la habita y que puede surgir como un relámpago cuando se siente "
    "amenazada, frustrada o ignorada. Sin embargo, también su entusiasmo, su pasión y su capacidad de luchar por lo que ama son igualmente "
    "intensos. En las relaciones, puede ser apasionada y protectora, pero también puede tener dificultades para gestionar la frustración "
    "sin estallar. Existe una necesidad profunda de afirmar su voluntad en el mundo, de abrirse camino a través de la vida con determinación, "
    "y cualquier obstáculo que se interponga entre ella y sus deseos despierta una respuesta combativa. La relación con la madre pudo haber "
    "sido intensa, quizás marcada por conflictos de poder, por una madre que era ella misma una luchadora, o por una dinámica donde la asertividad "
    "era necesaria para sobrevivir emocionalmente. La sombra de esta conjunción es la impulsividad: decir o hacer cosas en caliente de las que "
    "luego se arrepiente. El camino de crecimiento implica aprender a canalizar esta energía marciana de manera consciente, utilizando la ira "
    "como información y no como reacción. Cuando logra domar a su guerrero interno, esta persona se convierte en una fuerza imparable de "
    "transformación, capaz de defender sus límites con firmeza y de luchar por sus sueños con una pasión que inspira a quienes la rodean."
)

# Luna sextil Marte
ENTRIES["luna_sextil_marte"] = (
    "El sextil entre la Luna y Marte otorga una saludable capacidad para expresar la asertividad emocional y la iniciativa personal. "
    "Esta persona posee un coraje emocional que le permite enfrentar las situaciones difíciles sin paralizarse, y una energía vital que "
    "utiliza para construir la seguridad que necesita. No espera pasivamente a que la vida le proporcione lo que desea: sale a buscarlo, "
    "impulsada por una combinación equilibrada de deseo emocional y determinación activa. Existe una sincronía natural entre lo que siente "
    "y lo que hace, de modo que sus acciones suelen estar alineadas con sus necesidades emocionales más profundas. Esto le confiere una "
    "autenticidad que los demás perciben y respetan. En el trabajo y en los proyectos personales, muestra una iniciativa que la distingue, "
    "y no teme tomar riesgos calculados cuando su instinto emocional le indica que es el momento adecuado. La relación con la madre pudo "
    "haberla estimulado a ser independiente y a confiar en su propia fuerza, o bien encontró en ella un modelo de resiliencia que hoy "
    "la inspira. El riesgo de este aspecto armónico es que la persona puede volverse demasiado independiente emocionalmente, evitando "
    "pedir ayuda o mostrar vulnerabilidad por miedo a parecer débil. La oportunidad del sextil es precisamente encontrar el punto medio "
    "entre la autosuficiencia y la apertura al apoyo de los demás. Cuando la persona integra ambas dimensiones, su energía marciana se "
    "convierte en una herramienta al servicio de su crecimiento emocional y del servicio a los demás, sin perder por ello su propia fuerza."
)

# Luna cuadratura Marte
ENTRIES["luna_cuadratura_marte"] = (
    "La cuadratura entre la Luna y Marte instala un conflicto interno entre la necesidad de seguridad emocional y el impulso de afirmación "
    "personal. Esta persona vive en una tensión constante entre lo que necesita para sentirse segura y lo que desea en el calor del momento. "
    "Sus emociones son explosivas, y cuando se siente frustrada o amenazada, la ira emerge como una respuesta automática que a menudo "
    "daña las relaciones que más le importan. Puede arrepentirse amargamente de cosas dichas o hechas en momentos de enfado, pero en el "
    "calor del momento parece no tener control sobre sus reacciones. La infancia pudo haber estado marcada por un entorno donde la ira "
    "era la moneda de cambio emocional, quizás una madre impaciente o un ambiente familiar donde la agresividad era la forma de resolver "
    "los conflictos. Como resultado, la persona aprendió que la mejor defensa es un buen ataque, y que mostrar vulnerabilidad es peligroso. "
    "En las relaciones íntimas, esta dinámica se reproduce: puede atraer personas o situaciones que despiertan su ira, o bien elegir parejas "
    "que la provocan constantemente. Existe también una tendencia a somatizar la tensión emocional en forma de dolores de cabeza, problemas "
    "digestivos o tensión muscular. El camino de sanación implica aprender a reconocer las señales tempranas de la frustración antes de que "
    "se convierta en explosión, y encontrar formas constructivas de canalizar la energía marcial sin suprimirla. Deporte, terapia corporal, "
    "prácticas de respiración y expresión artística intensa pueden ser vehículos de integración. Cuando la persona aprende a estar en contacto "
    "con su ira sin actuar desde ella, descubre que su fuerza interior es su mayor aliada, no su enemiga."
)

# Luna trino Marte
ENTRIES["luna_trino_marte"] = (
    "El trino entre la Luna y Marte establece una corriente armoniosa entre las necesidades emocionales y la capacidad de actuar para "
    "satisfacerlas. Esta persona posee una valentía emocional innata, una confianza en su propio poder que le permite enfrentar los desafíos "
    "de la vida con determinación y optimismo. No se deja paralizar por el miedo ni por la inseguridad; cuando siente, actúa, y cuando actúa, "
    "lo hace con todo su ser. Existe una integración natural entre su mundo afectivo y su voluntad, de modo que sus acciones rara vez están "
    "en conflicto con lo que realmente necesita. Esto le confiere una autenticidad magnética que atrae a los demás y la convierte en una "
    "líder natural en aquellos ámbitos donde se requiere coraje emocional. La relación con la madre pudo haberla fortalecido, enseñándole "
    "a confiar en su propia fuerza y a no tener miedo de luchar por lo que quiere. En las relaciones, es apasionada pero no posesiva, "
    "intensa pero no violenta, y sabe cómo defender sus límites sin agredir. El peligro de este aspecto armónico es que la persona puede "
    "volverse demasiado confiada en su propia fuerza, olvidando que a veces la verdadera valentía está en la vulnerabilidad y en saber "
    "cuándo rendirse. El trino ofrece el don de la acción alineada con el corazón, pero la sabiduría exige que la persona no confunda "
    "la fuerza con la dureza. Cuando mantiene el corazón abierto mientras actúa con determinación, su poder se vuelve imparable y "
    "profundamente inspirador para quienes tienen la fortuna de presenciar su camino."
)

# Luna oposicion Marte
ENTRIES["luna_oposicion_marte"] = (
    "La oposición entre la Luna y Marte sitúa a la persona ante una polaridad constante entre su necesidad de seguridad emocional y su "
    "impulso de afirmarse a través de la acción. Estos dos principios parecen tirar en direcciones opuestas, generando una tensión que "
    "se manifiesta en las relaciones y en la forma de enfrentar los conflictos. Por un lado, la persona necesita cercanía, calidez y "
    "protección emocional; por otro, siente un impulso irrefrenable de independencia, de afirmar su voluntad y de abrirse camino sin "
    "depender de nadie. Esta división interna se proyecta con frecuencia en las parejas y en las figuras de autoridad, atrayendo "
    "relaciones donde el conflicto y la negociación de poder son protagonistas. Puede sentirse atraída por personas fuertes y "
    "dominantes, para luego resentir la falta de suavidad emocional, o bien elegir parejas sumisas que despiertan su frustración "
    "porque no pueden igualar su intensidad. La relación con la madre pudo haber sido conflictiva, marcada por dinámicas de poder "
    "donde la independencia y la dependencia se alternaban de manera confusa. El trabajo evolutivo de esta oposición es aprender a "
    "integrar ambos polos: desarrollar la capacidad de ser fuerte y tierna al mismo tiempo, de actuar desde la emoción y de sentir "
    "desde la acción. Las relaciones actúan como espejo de esta tensión, mostrando todo aquello que la persona no ha reconciliado en "
    "su interior. Cuando logra equilibrar la asertividad con la receptividad, descubre que su fuerza no amenaza su capacidad de amar, "
    "sino que la potencia. La oposición se convierte entonces en una fuente de energía dinámica que la impulsa a crecer sin perder "
    "su centro emocional."
)

# Luna conjuncion Jupiter
ENTRIES["luna_conjuncion_jupiter"] = (
    "Cuando la Luna y Júpiter se unen en conjunción, las emociones se expanden hasta ocupar todo el espacio disponible, como un océano "
    "que no conoce límites. Esta persona siente con una amplitud que abarca tanto el entusiasmo desbordante como la necesidad de encontrar "
    "sentido a todo lo que experimenta. Busca seguridad emocional no solo en las relaciones cercanas, sino en una conexión con algo más "
    "grande que ella misma: la filosofía, la espiritualidad, el conocimiento, el viaje, la exploración de horizontes que le devuelvan "
    "una sensación de pertenencia cósmica. Existe una generosidad emocional que la lleva a dar sin medida, a confiar con facilidad y a "
    "ver siempre el lado positivo de las personas y las situaciones, a veces en detrimento de su propio bienestar. La madre o la figura "
    "materna pudo haber sido una persona optimista, expansiva, quizás religiosa o filosófica, que le transmitió la creencia de que el "
    "mundo es un lugar abundante y benevolente. Sin embargo, esta misma expansión puede convertirse en su sombra: la tendencia a "
    "excederse, a no poner límites, a comer o gastar de más para llenar un vacío que nunca termina de colmarse. La persona puede "
    "tener dificultades para distinguir entre la generosidad genuina y la necesidad de ser querida a través de dar en exceso. "
    "El camino evolutivo implica aprender que la verdadera abundancia no está fuera, sino en la capacidad de sentirse plena desde "
    "dentro. Cuando logra equilibrar la expansión jupiteriana con la contención lunar, su optimismo se vuelve sabio y su generosidad "
    "se convierte en una fuerza sanadora que no solo la beneficia a ella, sino a todos los que tienen la suerte de cruzarse en su camino."
)

# Luna sextil Jupiter
ENTRIES["luna_sextil_jupiter"] = (
    "El sextil entre la Luna y Júpiter otorga una disposición emocional optimista y expansiva que abre puertas constantemente en la vida "
    "de la persona. Existe una confianza natural en que el universo proveerá, una fe en la bondad fundamental de la vida que le permite "
    "navegar las dificultades sin perder el horizonte. Esta persona encuentra seguridad emocional en el crecimiento, en la exploración "
    "de nuevas ideas, culturas y experiencias que amplían su comprensión del mundo. La rutina y el estancamiento la sofocan, mientras "
    "que el aprendizaje y el viaje la revitalizan. Posee una generosidad innata que se manifiesta tanto en lo material como en lo "
    "emocional: disfruta compartiendo lo que tiene y lo que sabe, y encuentra en el acto de dar una fuente profunda de satisfacción. "
    "Las relaciones suelen ser armoniosas porque la persona tiende a ver lo mejor de los demás y a crear un clima de confianza y "
    "apertura. La figura materna probablemente fue alentadora, quizás una fuente de inspiración filosófica o espiritual que le transmitió "
    "la certeza de que la vida es una aventura digna de ser vivida. El riesgo de este aspecto armónico es cierto exceso de optimismo "
    "que puede llevar a la ingenuidad o a la falta de realismo en asuntos prácticos. La oportunidad del sextil es aprender a equilibrar "
    "la confianza con la prudencia, utilizando la expansión jupiteriana para crecer sin perder el contacto con la tierra. Cuando logra "
    "este equilibrio, la persona descubre que su optimismo no es una ilusión, sino una fuerza creadora que atrae hacia ella las "
    "experiencias que necesita para seguir evolucionando."
)

# Luna cuadratura Jupiter
ENTRIES["luna_cuadratura_jupiter"] = (
    "La cuadratura entre la Luna y Júpiter revela una tensión entre la necesidad de seguridad emocional y el impulso de expandirse más "
    "allá de todo límite. Esta persona experimenta una insatisfacción crónica que la lleva a buscar siempre más: más comida, más dinero, "
    "más experiencias, más conocimiento, como si nunca pudiera sentirse realmente llena. Existe una tendencia a excederse en los placeres "
    "como forma de compensar un vacío emocional que no sabe cómo nombrar. La infancia pudo haber estado marcada por un exceso o una falta: "
    "quizás una madre sobreprotectora que lo daba todo sin enseñar a gestionar los límites, o por el contrario, una ausencia afectiva que "
    "la persona intenta llenar con cosas y experiencias. La relación con la figura materna puede haber sido ambivalente: generosa pero "
    "invasiva, o bien inspiradora pero ausente. En la vida adulta, la persona puede tener dificultades para manejar sus finanzas, "
    "para mantener hábitos saludables o para comprometerse con una sola dirección, pues siempre siente que podría haber algo mejor "
    "allá. La sombra de esta cuadratura es el exceso en todas sus formas, y el desafío está en aprender a encontrar satisfacción "
    "dentro de los límites de la realidad. El camino de crecimiento implica desarrollar una relación más consciente con la abundancia, "
    "reconociendo que la verdadera plenitud no está en la acumulación sino en la experiencia de suficiencia. Cuando la persona aprende "
    "a habitar el presente sin ansiedad de futuro, descubre que lo que realmente necesita ya está aquí, y que la expansión más "
    "auténtica no es la que va hacia afuera, sino la que nace desde adentro."
)

# Luna trino Jupiter
ENTRIES["luna_trino_jupiter"] = (
    "El trino entre la Luna y Júpiter establece una corriente de optimismo natural y abundancia emocional que impregna toda la vida "
    "de la persona. Esta configuración es una de las más afortunadas para la vida emocional, pues otorga una confianza innata en la "
    "bondad del universo y una capacidad para encontrar alegría incluso en las circunstancias más difíciles. La persona posee un "
    "sentido del humor que la protege de la desesperación y una fe en la vida que actúa como un imán para las oportunidades "
    "positivas. Su hogar emocional es amplio, acogedor, y tiende a extenderse para incluir no solo a la familia biológica sino "
    "también a amigos, mentores y toda persona que necesite un espacio seguro. La generosidad fluye de ella de manera espontánea, "
    "como un río que no necesita esfuerzo para correr. La relación con la madre fue probablemente nutritiva y alentadora, quizás "
    "una mujer sabia que le enseñó a confiar en la vida y a ver el vaso medio lleno. En las relaciones, busca personas que compartan "
    "su amor por la aventura y el crecimiento, y huye de quienes intentan limitar su libertad. El peligro de este trino es la "
    "tendencia a la complacencia: la persona puede confiar tanto en que todo saldrá bien que no toma las precauciones necesarias, "
    "o puede evitar enfrentar las sombras emocionales por miedo a perturbar su paz. La invitación del trino es utilizar la base "
    "de confianza y optimismo como plataforma para explorar también las dimensiones más complejas de la psique, integrando la "
    "sabiduría que nace de la adversidad sin perder la luz natural que la caracteriza."
)

# Luna oposicion Jupiter
ENTRIES["luna_oposicion_jupiter"] = (
    "La oposición entre la Luna y Júpiter crea una polaridad entre la necesidad de seguridad emocional hogareña y el impulso de "
    "expandirse hacia horizontes más amplios. Esta persona se encuentra oscilando entre el deseo de echar raíces, de crear un hogar "
    "seguro y estable, y la necesidad casi compulsiva de lanzarse a explorar el mundo, de buscar significado en experiencias que "
    "trasciendan lo cotidiano. Puede sentir que la vida hogareña la limita, pero cuando está lejos, extraña desesperadamente la "
    "calidez de un lugar al que pertenecer. Esta tensión se proyecta en las relaciones significativas, donde la persona puede "
    "sentirse atraída por parejas que le ofrecen expansión y aventura, pero que no le proporcionan la seguridad que necesita, "
    "o bien elegir parejas estables que luego le resultan aburridas. La relación con la madre pudo haber estado marcada por "
    "esta misma polaridad: quizás una mujer que sacrificó su propia expansión por la familia, o una madre que estuvo física o "
    "emocionalmente ausente porque estaba buscando su propio camino. El trabajo de esta oposición es integrar ambos mundos: "
    "aprender que se puede tener un hogar y al mismo tiempo un horizonte, que la seguridad no está reñida con la aventura. "
    "La persona necesita construir una base emocional sólida que no la ate, sino que le sirva como punto de partida para sus "
    "exploraciones. Cuando logra este equilibrio, descubre que el verdadero viaje no es el que la aleja de su hogar, sino el "
    "que la conecta más profundamente con él, y que la expansión más significativa es la que la lleva a conocerse a sí misma."
)

# Luna conjuncion Saturno
ENTRIES["luna_conjuncion_saturno"] = (
    "Cuando la Luna y Saturno se encuentran en conjunción, las emociones se tiñen de seriedad, responsabilidad y una profunda necesidad "
    "de control. Esta persona lleva en su interior una carga emocional que rara vez muestra al mundo: sus sentimientos son profundos, "
    "permanentes, pero difíciles de expresar con espontaneidad. Existe una sensación de haber tenido que madurar antes de tiempo, "
    "de haber aprendido desde la infancia que las emociones deben ser gestionadas con disciplina, que mostrar vulnerabilidad es "
    "un riesgo o una debilidad. La relación con la madre fue probablemente compleja: quizás fue una figura fría, distante, exigente, "
    "o bien alguien que imponía responsabilidades demasiado pronto. También pudo haber sido una madre que ella misma cargaba con "
    "una pesada carga emocional, incapaz de ofrecer la calidez y la contención que la niña necesitaba. Como resultado, la persona "
    "adulta se relaciona con sus propias emociones desde la reserva y el control. Tiende a minimizar sus necesidades afectivas, "
    "a sentirse culpable cuando prioriza su bienestar y a asumir cargas que no le corresponden porque ha aprendido que su valor "
    "depende de lo que hace por los demás. Sin embargo, esta misma conjunción otorga una capacidad de resistencia emocional "
    "extraordinaria, una lealtad inquebrantable hacia quienes ama y una profundidad psicológica que otras configuraciones no "
    "pueden igualar. El camino de crecimiento implica aprender a ablandarse, a permitirse sentir sin juzgarse, a recibir cuidado "
    "sin sentirse endeudada. Cuando logra integrar la calidez lunar con la disciplina saturnina, se convierte en una persona "
    "emocionalmente madura, confiable y profundamente sabia, alguien en quien los demás pueden apoyarse sin reservas."
)

# Luna sextil Saturno
ENTRIES["luna_sextil_saturno"] = (
    "El sextil entre la Luna y Saturno otorga una capacidad natural para gestionar las emociones con madurez y responsabilidad. "
    "Esta persona posee una estabilidad emocional que le permite enfrentar las dificultades de la vida sin desmoronarse, y una "
    "disciplina afectiva que la ayuda a construir relaciones sólidas y duraderas. No teme el compromiso ni la responsabilidad "
    "emocional; al contrario, encuentra seguridad en la estructura y en la claridad de los roles y las expectativas. Existe "
    "una sensación de haber aprendido desde pequeña que las emociones no son algo peligroso o caótico, sino que pueden ser "
    "gestionadas con cuidado y respeto. La figura materna probablemente fue una fuente de estabilidad y enseñanzas prácticas, "
    "alguien que supo transmitirle la importancia de la paciencia, la perseverancia y el trabajo emocional constante. Esta "
    "configuración abre oportunidades para desarrollar una carrera en ámbitos donde se requiere madurez emocional: la psicología, "
    "el trabajo social, la educación, la gestión de equipos humanos. La persona sabe cómo poner límites sin culpa y cómo cuidar "
    "de los demás sin descuidarse a sí misma. El riesgo de este aspecto armónico es que la persona puede volverse demasiado "
    "rígida emocionalmente, suprimiendo la espontaneidad afectiva en nombre del control y la responsabilidad. La oportunidad "
    "del sextil es aprender a equilibrar la disciplina saturnina con la flexibilidad lunar, permitiéndose ser seria pero no "
    "severa, responsable pero no rígida. Cuando encuentra este equilibrio, su madurez emocional se convierte en un don que "
    "ofrece a los demás un espacio seguro donde crecer sin miedo."
)

# Luna cuadratura Saturno
ENTRIES["luna_cuadratura_saturno"] = (
    "La cuadratura entre la Luna y Saturno revela una herida profunda en la capacidad de sentir seguridad y de expresar las "
    "necesidades emocionales. Esta persona creció en un entorno donde las emociones no eran bienvenidas, donde la vulnerabilidad "
    "era castigada o ridiculizada, y donde probablemente tuvo que aprender a cuidar de sí misma muy pronto porque nadie más lo "
    "hacía. La relación con la madre fue difícil: pudo haber sido una figura ausente, fría, crítica o emocionalmente inaccesible, "
    "alguien que imponía estándares imposibles de cumplir o que simplemente no tenía la capacidad de ofrecer el calor y la "
    "contención que la niña necesitaba. Como resultado, la persona adulta carga con un peso emocional que no sabe cómo soltar: "
    "una sensación de no ser digna de amor, de tener que ganarse el afecto a través del esfuerzo y el sacrificio. Tiende a "
    "autocríticarse ferozmente, a minimizar sus logros y a magnificar sus fracasos. En las relaciones, puede ser reservada, "
    "desconfiada, o bien buscar parejas que reproducen la dinámica de frialdad afectiva que conoció en la infancia. El miedo "
    "al rechazo es tan profundo que a menudo prefiere no intentarlo antes de arriesgarse a ser herida. Sin embargo, esta "
    "configuración contiene la semilla de una fuerza emocional extraordinaria. Cuando la persona se decide a sanar, desarrolla "
    "una comprensión de la psique humana que pocos pueden igualar, una capacidad de sostener el dolor propio y ajeno con "
    "dignidad y una resiliencia forjada en el fuego del sufrimiento consciente. El camino implica aprender a ser la madre "
    "que no tuvo, a ofrecerse a sí misma la calidez y la aceptación incondicional que tanto necesita."
)

# Luna trino Saturno
ENTRIES["luna_trino_saturno"] = (
    "El trino entre la Luna y Saturno establece una corriente de madurez emocional y responsabilidad afectiva que fluye de manera "
    "natural en la vida de la persona. Esta configuración otorga una capacidad innata para gestionar las emociones con serenidad, "
    "para mantener la calma en medio de la tormenta y para construir relaciones basadas en el compromiso real, no en la fantasía "
    "romántica. La persona sabe que el amor verdadero no es solo sentimiento, sino también elección, paciencia y trabajo constante. "
    "Existe una sensación de haber contado con una base familiar estable y segura, quizás una madre que supo combinar la disciplina "
    "con el cariño, o un entorno donde se valoraba tanto la responsabilidad como la conexión emocional. La persona posee una "
    "relación saludable con la autoridad y con las estructuras, y tiende a ser alguien en quien los demás confían naturalmente "
    "por su fiabilidad y su sentido del deber. En el ámbito laboral y social, se distingue por su capacidad de mantener la "
    "compostura bajo presión y de tomar decisiones difíciles sin evadir la carga emocional que conllevan. El peligro de este "
    "aspecto armónico es cierta tendencia a la rigidez emocional, a confundir la madurez con la supresión de la espontaneidad "
    "afectiva. La persona puede volverse demasiado seria, demasiado controlada, perdiendo la conexión con la alegría simple y "
    "la vulnerabilidad que hace que las relaciones sean profundas. El trino ofrece la estructura, pero la sabiduría exige "
    "que la persona no olvide habitar también la fluidez del corazón. Cuando integra la solidez saturnina con la receptividad "
    "lunar, se convierte en un pilar emocional para todos los que la rodean, sin perder por ello su propia calidez interior."
)

# Luna oposicion Saturno
ENTRIES["luna_oposicion_saturno"] = (
    "La oposición entre la Luna y Saturno sitúa a la persona en una polaridad constante entre su necesidad de seguridad emocional "
    "y su sentido del deber y la responsabilidad. Existe un conflicto interno entre lo que necesita para sentirse nutrida y lo "
    "que cree que debe hacer para ser aceptada y valorada. Esta persona puede sentir que el amor y la responsabilidad son "
    "incompatibles, que para ser digna de afecto debe sacrificar sus propias necesidades, o que si atiende sus necesidades "
    "emocionales descuidará sus obligaciones. La relación con la madre fue compleja: quizás una figura que alternaba entre la "
    "sobreprotección y la frialdad, o alguien que imponía expectativas tan altas que el amor quedaba condicionado al logro. "
    "También pudo haber sido una madre ausente, ya sea física o emocionalmente, que obligó a la persona a crecer demasiado "
    "rápido y a asumir responsabilidades adultas antes de tiempo. En la vida adulta, esta polaridad se manifiesta en las "
    "relaciones de pareja y en la vida laboral: la persona puede elegir parejas que representan la autoridad o la frialdad "
    "que conoció en la infancia, o bien puede ella misma asumir el rol de la responsable que nunca recibe el cuidado que "
    "necesita. También puede oscilar entre períodos de hiperresponsabilidad y momentos de rebeldía donde abandona todas sus "
    "obligaciones. El trabajo de esta oposición es aprender a integrar ambos mundos, reconociendo que la responsabilidad y "
    "el cuidado emocional no son opuestos sino complementarios. Cuando la persona logra construir relaciones donde puede ser "
    "tanto responsable como vulnerable, tanto adulta como niña necesitada de cuidado, descubre que la verdadera madurez "
    "no está en la rigidez, sino en la capacidad de habitar todas las dimensiones del ser."
)

# Luna conjuncion Urano
ENTRIES["luna_conjuncion_urano"] = (
    "Cuando la Luna y Urano se fusionan en conjunción, las emociones se vuelven eléctricas, impredecibles y radicalmente libres. "
    "Esta persona no puede sentir de manera convencional ni encontrar seguridad en la rutina emocional. Sus estados de ánimo "
    "cambian con una rapidez que desconcierta tanto a ella como a quienes la rodean, y necesita espacios de libertad dentro "
    "de cualquier vínculo afectivo para no sofocarse. Existe una necesidad profunda de autenticidad que rechaza cualquier "
    "forma de hipocresía emocional o de tradición impuesta. Desde la infancia, probablemente sintió que no encajaba en el "
    "molde familiar, que su forma de sentir y de expresar el afecto era diferente, extraña incluso. La relación con la madre "
    "pudo haber sido inusual: una madrebohemia, excéntrica, impredecible, o bien una figura que rompió las reglas de alguna "
    "manera significativa. La persona adulta busca relaciones que respeten su necesidad de independencia y que estimulen su "
    "mente tanto como su corazón. Las relaciones convencionales, con horarios y expectativas fijas, la asfixian. Su intuición "
    "es poderosa, casi psíquica en momentos de alta tensión emocional, y tiene una capacidad para percibir las verdades "
    "ocultas de las personas y las situaciones. La sombra de esta conjunción es la inestabilidad emocional y la tendencia "
    "a cortar vínculos de manera abrupta cuando se siente atrapada. El camino de crecimiento implica aprender a integrar "
    "la necesidad de libertad con la capacidad de compromiso, descubriendo que la verdadera autonomía no está en la huida, "
    "sino en la posibilidad de elegir conscientemente estar con alguien sin perder la propia identidad."
)

# Luna sextil Urano
ENTRIES["luna_sextil_urano"] = (
    "El sextil entre la Luna y Urano otorga una apertura mental y emocional a lo nuevo, lo diferente y lo innovador. Esta "
    "persona posee una capacidad natural para adaptarse a los cambios emocionales sin aferrarse al pasado, y una intuición "
    "que le permite percibir las corrientes subterráneas de la realidad antes de que se manifiesten. La necesidad de libertad "
    "y de autenticidad está presente, pero no de manera conflictiva: existe una integración armoniosa entre su necesidad de "
    "seguridad emocional y su deseo de explorar caminos alternativos. En las relaciones, valora la honestidad radical y la "
    "posibilidad de ser ella misma sin máscaras, y tiende a atraer personas que también valoran la libertad y la originalidad. "
    "La figura materna pudo haber sido una mujer adelantada a su tiempo, alguien que le enseñó a pensar por sí misma y a no "
    "seguir las normas solo porque sí. Esta configuración abre oportunidades para desarrollar talentos en campos innovadores "
    "o alternativos: la tecnología, la astrología, la psicología transpersonal, las terapias alternativas, cualquier ámbito "
    "que combine la sensibilidad emocional con una visión vanguardista. El riesgo de este aspecto armónico es cierta tendencia "
    "a la dispersión emocional: la persona puede entusiasmarse con muchas cosas y personas, pero tener dificultades para "
    "mantener el interés a largo plazo. La oportunidad del sextil es aprender a equilibrar la apertura a lo nuevo con la "
    "profundidad que requiere el compromiso emocional genuino. Cuando la persona integra ambas dimensiones, su vida emocional "
    "se convierte en una aventura fascinante donde la libertad y la conexión profunda no son excluyentes."
)

# Luna cuadratura Urano
ENTRIES["luna_cuadratura_urano"] = (
    "La cuadratura entre la Luna y Urano instala una tensión fundamental entre la necesidad de seguridad emocional y el impulso "
    "de libertad radical. Esta persona experimenta una contradicción interna que la lleva a sabotear sus propias relaciones "
    "justo cuando empiezan a volverse estables. Necesita cercanía, pero cuando la encuentra, siente que la atrapan. Desea la "
    "intimidad, pero cuando la consigue, busca desesperadamente una salida. La infancia estuvo marcada probablemente por "
    "rupturas imprevistas, cambios bruscos en el entorno familiar o una madre impredecible cuyos estados de ánimo alternaban "
    "entre la cercanía intensa y la distancia repentina. Como resultado, la persona aprendió a no confiar en la estabilidad "
    "emocional y desarrolló mecanismos de defensa que la mantienen siempre alerta, lista para la próxima interrupción. "
    "En la vida adulta, esta dinámica se reproduce: puede atraer parejas poco convencionales, relaciones a distancia o "
    "situaciones amorosas marcadas por la intermitencia y la incertidumbre. Existe un talento innato para percibir lo que "
    "otros no ven, una intuición que opera como un radar emocional, pero también una tendencia a reaccionar de manera "
    "explosiva cuando se siente limitada. El camino de sanación implica aprender a crear estabilidad sin sacrificar la "
    "autenticidad, a comprometerse sin perderse. La persona necesita encontrar formas de expresar su individualidad dentro "
    "de las relaciones, no fuera de ellas. Cuando logra reconciliar la necesidad de libertad con el deseo de pertenencia, "
    "se convierte en un puente entre dos mundos, capaz de amar sin poseer y de estar presente sin sentirse atrapada."
)

# Luna trino Urano
ENTRIES["luna_trino_urano"] = (
    "El trino entre la Luna y Urano establece una corriente natural de originalidad emocional y libertad intuitiva que fluye "
    "sin esfuerzo en la vida de la persona. Esta configuración otorga una capacidad única para sentir y expresar las emociones "
    "de manera auténtica, sin las ataduras de las convenciones sociales. La persona no necesita rebelarse para ser libre: "
    "su libertad es tan natural que no requiere ser defendida, solo vivida. Posee una intuición que funciona como un sexto "
    "sentido, captando información del ambiente y de las personas que otros pasan por alto. En las relaciones, es abierta, "
    "tolerante y respeta profundamente la individualidad del otro. No busca poseer ni ser poseída, sino compartir desde la "
    "autonomía y el respeto mutuo. La relación con la madre fue probablemente poco convencional pero positiva: quizás una "
    "mujer que valoraba la independencia y alentaba a su hija a pensar por sí misma, o alguien que le transmitió la confianza "
    "necesaria para ser diferente sin sentir culpa. La persona tiende a rodearse de amistades diversas y estimulantes, y "
    "encuentra seguridad emocional en la variedad y en la posibilidad de crecimiento constante. El peligro de este trino "
    "es la tendencia a evitar el compromiso profundo precisamente porque la libertad se siente tan bien. La persona puede "
    "quedarse en la superficie de las relaciones, moviéndose de una experiencia a otra sin echar raíces verdaderas. "
    "El trino ofrece el don de la libertad auténtica, pero la sabiduría exige que la persona elija conscientemente cuándo "
    "y con quién profundizar. Cuando lo hace, su vida emocional es una danza única entre la conexión y la autonomía."
)

# Luna oposicion Urano
ENTRIES["luna_oposicion_urano"] = (
    "La oposición entre la Luna y Urano crea una polaridad vibrante entre la necesidad de seguridad emocional y el impulso "
    "de libertad e independencia. Esta persona se encuentra en un tira y afloja constante entre el deseo de echar raíces y "
    "la necesidad de volar, entre la comodidad de lo conocido y la excitación de lo inesperado. Las relaciones significativas "
    "suelen ser el escenario donde esta tensión se representa: puede sentirse atraída por personas impredecibles y libres, "
    "para luego resentir su falta de disponibilidad emocional, o bien elegir parejas estables que luego le resultan "
    "demasiado predecibles y aburridas. La relación con la madre estuvo marcada por la imprevisibilidad: quizás una mujer "
    "que aparecía y desaparecía emocionalmente, o alguien cuya forma de amar era tan poco convencional que la niña nunca "
    "supo bien a qué atenerse. En la vida adulta, la persona puede tener una relación ambivalente con su propio hogar: "
    "lo ama y lo odia, lo construye y lo desmantela, cambia de residencia con frecuencia o mantiene su espacio en un "
    "estado constante de reorganización. El trabajo de esta oposición es aprender a integrar ambos polos, descubriendo "
    "que la verdadera seguridad no está en la rigidez de lo estable, sino en la confianza en la propia capacidad de "
    "adaptarse a los cambios. Las relaciones actúan como espejo de esta integración: cuando logra estar presente sin "
    "aferrarse y libre sin huir, descubre que puede mantener vínculos profundos sin sacrificar su individualidad. "
    "La oposición se convierte entonces en una fuente de creatividad y originalidad que enriquece todas sus relaciones."
)

# Luna conjuncion Neptuno
ENTRIES["luna_conjuncion_neptuno"] = (
    "Cuando la Luna y Neptuno se encuentran en conjunción, las emociones se disuelven en un océano de sensibilidad sin límites. "
    "Esta persona no solo siente: absorbe las emociones del entorno como una esponja, confundiendo con frecuencia lo que es "
    "suyo con lo que pertenece a los demás. Existe una permeabilidad psíquica que la hace vulnerable a la atmósfera emocional "
    "de los lugares y las personas, una capacidad de empatía que puede llegar a ser abrumadora cuando no está gestionada. "
    "Desde la infancia, probablemente fue una niña hipersensible, capaz de percibir las tensiones no dichas del hogar y "
    "de cargar con ellas como si fueran propias. La relación con la madre pudo haber sido difusa, confusa, quizás marcada "
    "por la idealización o la decepción: una madre que no estuvo del todo presente, o que estaba presente de una manera "
    "tan etérea que nunca se pudo establecer un vínculo sólido y claro. La persona adulta busca en las relaciones una "
    "fusión espiritual, una conexión que trascienda lo ordinario, y puede sentirse profundamente decepcionada cuando la "
    "realidad no está a la altura de sus fantasías. Existe un talento artístico y espiritual muy desarrollado: la música, "
    "la poesía, la fotografía, las prácticas mediúmnicas o cualquier forma de expresión que canalice lo intangible. Sin "
    "embargo, la sombra de esta conjunción es la tendencia a la evasión: el escapismo a través del sueño, las drogas, "
    "la fantasía o la idealización del otro. El camino de crecimiento implica aprender a discriminar entre la realidad "
    "y la proyección, a desarrollar límites psíquicos saludables sin perder la sensibilidad, y a encontrar formas "
    "concretas de expresar su profunda conexión con lo sagrado sin perderse en él."
)

# Luna sextil Neptuno
ENTRIES["luna_sextil_neptuno"] = (
    "El sextil entre la Luna y Neptuno otorga una sensibilidad psíquica y una imaginación emocional que pueden ser canalizadas "
    "de manera creativa y constructiva. Esta persona posee una empatía natural que le permite comprender a los demás en un "
    "nivel profundo, casi telepático, y una capacidad para percibir las corrientes emocionales invisibles que fluyen entre "
    "las personas. Existe una apertura a la dimensión espiritual de la vida que le proporciona un sentido de conexión con "
    "algo más grande que ella misma, una fuente de consuelo y significado que trasciende las dificultades cotidianas. "
    "La figura materna pudo haber sido una mujer sensible, artística o espiritualmente inclinada, que le transmitió la "
    "importancia de la compasión y la belleza como valores fundamentales. Esta configuración abre oportunidades para "
    "desarrollar talentos en las artes, la música, la danza, la fotografía o cualquier expresión que canalice la emoción "
    "a través de la forma. También favorece el trabajo terapéutico o de acompañamiento espiritual, donde la capacidad "
    "de sintonizar con los estados internos de los demás es un don invaluable. El riesgo de este aspecto armónico es "
    "que la persona puede refugiarse demasiado en el mundo de la fantasía y la espiritualidad como forma de evitar "
    "los desafíos concretos de la vida material. La oportunidad del sextil es aprender a equilibrar la sensibilidad "
    "neptuniana con el anclaje en la realidad, utilizando la imaginación no como escape, sino como herramienta de "
    "creación y sanación. Cuando logra este equilibrio, su presencia es profundamente sanadora para quienes la rodean."
)

# Luna cuadratura Neptuno
ENTRIES["luna_cuadratura_neptuno"] = (
    "La cuadratura entre la Luna y Neptuno revela una herida en la capacidad de discriminar entre la realidad y la fantasía, "
    "entre las propias emociones y las de los demás. Esta persona creció en un entorno emocional confuso, donde los límites "
    "eran difusos y las señales afectivas contradictorias. La madre pudo haber sido una figura etérea, ausente o víctima de "
    "adicciones, alguien que no podía ofrecer una presencia clara y consistente. También pudo haber sido una madre que "
    "idealizaba a su hija, proyectando sobre ella expectativas irreales que la niña nunca podía cumplir. Como resultado, "
    "la persona adulta tiene dificultades para saber lo que realmente siente y para distinguir sus emociones de las que "
    "absorbe del entorno. Tiende a idealizar las relaciones y a sufrir profundas decepciones cuando la realidad se impone. "
    "Puede tener una tendencia a la dependencia emocional, a buscar parejas que la rescaten o que la confundan, reproduciendo "
    "la dinámica de imprevisibilidad afectiva que conoció en la infancia. Existe también una tendencia a la evasión: "
    "el alcohol, las drogas, los fármacos, la comida o simplemente la ensoñación excesiva pueden ser formas de escapar "
    "de un dolor emocional que no sabe cómo gestionar. Sin embargo, esta cuadratura contiene la semilla de una sensibilidad "
    "extraordinaria. Cuando la persona emprende el camino de sanación, desarrolla una capacidad de empatía y compasión "
    "que pocos pueden igualar, un talento artístico que puede conmover a otros y una conexión espiritual que no necesita "
    "de intermediarios. El camino implica aprender a poner límites psíquicos, a anclar la sensibilidad en la realidad "
    "y a distinguir entre el amor real y la fantasía de salvación."
)

# Luna trino Neptuno
ENTRIES["luna_trino_neptuno"] = (
    "El trino entre la Luna y Neptuno establece una corriente de sensibilidad poética y percepción psíquica que fluye "
    "de manera natural en la vida de la persona. Esta configuración otorga una capacidad innata para conectar con las "
    "dimensiones más sutiles de la existencia, para percibir la belleza donde otros solo ven lo ordinario y para "
    "sentir compasión de una manera que trasciende el mero entendimiento intelectual. La persona posee una imaginación "
    "emocional que enriquece todo lo que toca: su hogar, sus relaciones, su trabajo. Existe una sensación de haber "
    "estado en contacto con algo sagrado desde la infancia, quizás a través de una madre que cultivaba la espiritualidad "
    "o el arte, o simplemente a través de una conexión innata con la naturaleza y el mundo de los sueños. En las "
    "relaciones, es profundamente empática y compasiva, capaz de estar presente con el dolor ajeno sin sentirse "
    "abrumada, y de ofrecer un espacio de aceptación incondicional. Su intuición es fina y precisa, y confiar en ella "
    "le ahorra muchos errores que otros cometen por exceso de racionalidad. El peligro de este trino es que la persona "
    "puede volverse demasiado pasiva, confiando tanto en el flujo natural de la vida que no toma las riendas de su "
    "propia existencia. También puede tender a idealizar a las personas, viéndolas a través de un velo de fantasía "
    "que tarde o temprano se rompe. El trino ofrece el don de la conexión con lo divino, pero la sabiduría exige "
    "que la persona no se pierda en el océano de la sensibilidad, sino que aprenda a navegarlo con conciencia. "
    "Cuando integra la compasión neptuniana con el discernimiento, se convierte en una fuente de inspiración y "
    "sanación para todos los que cruzan su camino."
)

# Luna oposicion Neptuno
ENTRIES["luna_oposicion_neptuno"] = (
    "La oposición entre la Luna y Neptuno sitúa a la persona en una polaridad constante entre la necesidad de claridad "
    "emocional y la atracción por lo misterioso, lo indefinido y lo trascendente. Existe un conflicto entre el deseo "
    "de tener relaciones claras y definidas y la tendencia a perderse en la confusión emocional y la idealización "
    "del otro. La persona puede sentirse dividida entre el mundo concreto de las relaciones cotidianas y un anhelo "
    "profundo de fusión espiritual que ninguna relación parece satisfacer plenamente. La relación con la madre estuvo "
    "marcada por la confusión y la falta de límites claros: quizás una madre que alternaba entre la sobreimplicación "
    "emocional y la distancia, o alguien que proyectaba sus propias fantasías no resueltas sobre la hija. También "
    "pudo haber sido una figura víctima de adicciones o de enfermedades que la hacían impredecible e inaccesible. "
    "En la vida adulta, la persona puede tener una tendencia a repetir estas dinámicas en sus relaciones íntimas: "
    "atrae personas que necesitan ser rescatadas, que son emocionalmente confusas o que desaparecen cuando las "
    "cosas se ponen difíciles. Existe también una sensibilidad artística y espiritual muy desarrollada, pero "
    "también una tendencia a la evasión y a la confusión entre el amor real y la fantasía romántica. El trabajo "
    "de esta oposición es aprender a integrar ambos mundos: honrar la necesidad de trascendencia sin perder el "
    "contacto con la realidad, cultivar la sensibilidad sin caer en la confusión, y construir relaciones que "
    "puedan contener tanto la magia como la verdad cotidiana. Cuando logra este equilibrio, descubre que lo "
    "sagrado no está fuera de las relaciones humanas, sino en el corazón mismo de la conexión auténtica."
)

# Luna conjuncion Pluton
ENTRIES["luna_conjuncion_pluton"] = (
    "Cuando la Luna y Plutón se fusionan en conjunción, las emociones adquieren una intensidad que todo lo penetra y lo "
    "transforma. Esta persona siente como si estuviera habitada por fuerzas emocionales que la superan: pasiones que "
    "la consumen, miedos que la paralizan y una capacidad de regeneración que la obliga a renacer una y otra vez. "
    "No hay término medio en su mundo afectivo; todo se vive al límite, como si la vida y la muerte emocional "
    "estuvieran siempre presentes en cada experiencia significativa. La infancia estuvo marcada probablemente por "
    "experiencias emocionales intensas y transformadoras: una madre poderosa, dominante o víctima de circunstancias "
    "traumáticas, una dinámica familiar donde el control y la manipulación eran moneda corriente, o quizás una "
    "pérdida temprana que marcó su relación con la seguridad y el apego. Como resultado, la persona adulta desarrolla "
    "una necesidad de control emocional que puede manifestarse como una tendencia a investigar los secretos de los "
    "demás, a manipular situaciones para sentirse segura o a aferrarse a las relaciones con una intensidad que "
    "asusta. Existe un miedo profundo a la traición y al abandono, y una capacidad casi detectivesca para percibir "
    "las motivaciones ocultas de las personas. Sin embargo, esta misma intensidad le otorga una capacidad de "
    "transformación extraordinaria: cuando se enfrenta a sus sombras, la persona puede renacer de sus cenizas "
    "con una fuerza y una sabiduría que inspiran a todos los que presencian su proceso. El camino implica aprender "
    "a manejar el poder emocional sin abusar de él, a soltar el control sin sentirse vulnerable y a confiar en "
    "la vida sabiendo que cada muerte emocional trae consigo una nueva oportunidad de renacer."
)

# Luna sextil Pluton
ENTRIES["luna_sextil_pluton"] = (
    "El sextil entre la Luna y Plutón otorga una profundidad emocional y una capacidad de autoconocimiento que permite "
    "a la persona acceder a las capas más ocultas de su psique con relativa facilidad. Existe una relación natural con "
    "el poder emocional, una comprensión intuitiva de que las emociones más oscuras no son enemigas sino aliadas en "
    "el proceso de crecimiento. Esta persona no teme mirar dentro de sí misma, no huye de la sombra, sino que sabe "
    "que en las profundidades del inconsciente se encuentran las llaves de su transformación. Esta configuración abre "
    "oportunidades para el trabajo psicológico profundo, ya sea como paciente o como terapeuta, y para todas aquellas "
    "actividades que requieran investigar lo oculto: la psicología, la investigación, el periodismo de profundidad, "
    "la astrología, la terapia de sombra. La relación con la madre fue intensa pero no necesariamente traumática: "
    "quizás una mujer fuerte y poderosa que le transmitió la importancia de conocerse a sí misma y de no temer al "
    "cambio. En las relaciones, la persona busca conexiones que tengan profundidad y significado, y tiene poco "
    "interés en los vínculos superficiales. Necesita sentir que la relación es un vehículo de transformación mutua, "
    "y tiende a atraer personas que también están comprometidas con su propio crecimiento. El riesgo de este aspecto "
    "armónico es cierta tendencia a la intensidad excesiva, a querer penetrar en los secretos del otro antes de "
    "tiempo o a tomarse las cosas demasiado en serio. La oportunidad del sextil es aprender a dosificar la intensidad, "
    "utilizando la profundidad emocional no para controlar, sino para comprender. Cuando logra este equilibrio, "
    "su presencia es magnética y profundamente transformadora para quienes la rodean."
)

# Luna cuadratura Pluton
ENTRIES["luna_cuadratura_pluton"] = (
    "La cuadratura entre la Luna y Plutón revela una herida emocional profunda relacionada con el poder, el control y "
    "la intensidad afectiva. Esta persona vivió en la infancia experiencias emocionales que la marcaron para siempre: "
    "quizás una madre dominante que ejercía un control excesivo, una dinámica familiar donde la manipulación emocional "
    "era la norma, o situaciones de pérdida, abuso o abandono que dejaron cicatrices en su psique. Como resultado, "
    "la persona adulta desarrolla una relación compleja con el poder emocional. Puede sentirse víctima de sus propias "
    "emociones, que la desbordan con una intensidad que no sabe gestionar, o puede haber aprendido a controlar "
    "compulsivamente su entorno afectivo como forma de protegerse de la vulnerabilidad. En las relaciones, tiende "
    "a reproducir dinámicas de poder: atrae parejas dominantes o controladoras, o ella misma asume ese rol, "
    "convirtiendo el amor en un campo de batalla donde la confianza es difícil de establecer. Existe una tendencia "
    "a los celos posesivos, a la desconfianza y a la necesidad de saberlo todo sobre el otro como forma de sentirse "
    "segura. Sin embargo, esta cuadratura contiene un potencial transformador inmenso. Cuando la persona se decide a "
    "sanar, desarrolla una comprensión de la psique humana que pocos pueden alcanzar, una capacidad de renacer de "
    "las cenizas de sus propias crisis y una fuerza emocional que la convierte en un pilar para quienes atraviesan "
    "procesos difíciles. El camino implica aprender a soltar el control, a confiar en el otro sin perderse, "
    "y a utilizar la intensidad emocional como combustible para la transformación consciente, no para la destrucción."
)

# Luna trino Pluton
ENTRIES["luna_trino_pluton"] = (
    "El trino entre la Luna y Plutón establece una corriente natural de profundidad emocional y poder transformador que "
    "fluye sin esfuerzo en la vida de la persona. Esta configuración otorga una capacidad innata para acceder a las "
    "dimensiones más profundas de la psique, para comprender los mecanismos ocultos del comportamiento humano y "
    "para transformar las experiencias dolorosas en sabiduría. La persona posee una resiliencia emocional que "
    "parece no tener límites: puede atravesar las crisis más intensas y salir fortalecida, como si llevara dentro "
    "un manantial inagotable de renovación. Existe una relación sana con el poder: no teme su propia fuerza ni "
    "necesita imponerla sobre los demás, sino que la utiliza con conciencia y responsabilidad. La relación con "
    "la madre fue intensa pero no destructiva: quizás una mujer de gran fortaleza interior que le enseñó a no "
    "temer a las profundidades de la vida, o alguien que, a través de su propio proceso de transformación, "
    "le mostró que es posible renacer de cualquier adversidad. En las relaciones, la persona busca vínculos "
    "que tengan sustancia, que la desafíen a crecer y que ofrezcan un espacio seguro para la vulnerabilidad "
    "más auténtica. No le interesan las relaciones superficiales; necesita sentir que el vínculo tiene la "
    "capacidad de transformar a ambos. El peligro de este trino es cierta tendencia a buscar la intensidad "
    "por la intensidad misma, a crear drama donde no lo hay para sentirse viva, o a involucrarse en relaciones "
    "demasiado complejas solo por el desafío que representan. El trino ofrece el don de la transformación "
    "consciente, pero la sabiduría exige que la persona aprenda a aplicar esta capacidad también en la "
    "sencillez del día a día, no solo en las crisis. Cuando lo logra, su presencia es inolvidable."
)

# Luna oposicion Pluton
ENTRIES["luna_oposicion_pluton"] = (
    "La oposición entre la Luna y Plutón sitúa a la persona en una polaridad constante entre su necesidad de seguridad "
    "emocional y el poder transformador que irrumpe en su vida a través de las relaciones significativas. Existe "
    "una tensión entre el deseo de tener una vida emocional estable y predecible y la atracción magnética hacia "
    "personas y situaciones que desencadenan crisis y transformación. La persona puede sentir que sus relaciones "
    "íntimas son un campo minado donde el poder, los celos y la necesidad de control emergen inevitablemente. "
    "La relación con la madre estuvo marcada por dinámicas de poder intensas: quizás una relación de amor-odio, "
    "una madre que ejercía un control excesivo o que era emocionalmente abusiva, o una situación familiar donde "
    "los secretos y las manipulaciones eran la moneda corriente. Como resultado, la persona adulta proyecta esta "
    "dinámica en sus relaciones de pareja, atrayendo a personas que representan el poder, la intensidad y "
    "el desafío, o convirtiéndose ella misma en vehículo de transformación para otros. Puede tener una tendencia "
    "a involucrarse en relaciones codependientes, donde los límites son difusos y la fusión emocional es intensa "
    "y a menudo dolorosa. El trabajo de esta oposición es aprender a integrar ambos polos: desarrollar la capacidad "
    "de estar en relaciones íntimas sin perderse, de manejar el poder sin abusar de él y de transformar sin "
    "destruir. Las relaciones actúan como espejo de las sombras no resueltas, y cada conflicto es una oportunidad "
    "para sanar las heridas del pasado. Cuando la persona logra integrar la intensidad plutoniana con la "
    "receptividad lunar, descubre que puede amar sin poseer, transformar sin romper y estar presente en la "
    "crisis sin perder su centro emocional. Su capacidad de acompañar a otros en procesos de transformación "
    "profunda se convierte entonces en su mayor don."
)

# --- WRITE JSON ---
filepath = '/home/pipe/Documents/proyectos/cartas_natales/datos/aspectos.json'
with open(filepath, 'r') as f:
    data = json.load(f)

for key, val in ENTRIES.items():
    if key in data:
        data[key] = val
        print(f"✓ Replaced {key} ({len(val)} chars)")
    else:
        print(f"✗ Key not found: {key}")

with open(filepath, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Successfully replaced {len(ENTRIES)} luna_* entries in aspectos.json")
