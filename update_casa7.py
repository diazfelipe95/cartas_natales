import json
import sys

FILE = "/home/pipe/Documents/proyectos/cartas_natales/datos/casas_signos.json"

ENTRIES = {
    "casa_7_aries": """Casa 7 en Aries

Quienes tienen la Casa 7 en Aries se acercan a las relaciones con la misma energia impulsiva y directa con la que este signo de fuego aborda la vida. No hay en ellos paciencia para los juegos ni para las expectativas sociales que dictan como debe conducirse una pareja. Cuando se interesan por alguien, lo demuestran con una franqueza que puede resultar abrumadora, y esperan del otro la misma honestidad sin reservas que ellos ofrecen. La relacion es un campo de exploracion donde la independencia personal no se negocia, y donde la chispa inicial es tan importante como la libertad para ser quienes son.

La imagen que proyectan en la pareja es la de alguien apasionado, valiente y emocionante que no teme dar el primer paso ni perseguir lo que desea. Los demas las perciben como personas que saben lo que quieren en una relacion y que no se conforman con menos de lo que merecen. Pueden parecer intensas o incluso dominantes, pero su energia es simplemente la manifestacion de un corazon que se entrega sin reservas cuando realmente esta comprometido.

El conflicto interno de esta posicion es la tension entre la necesidad de union y el miedo a perder la independencia. Estas personas pueden sentirse atraidas por relaciones intensas pero luego sentir que su libertad esta amenazada. La impaciencia las lleva a veces a apresurar las etapas de la relacion o a querer resultados inmediatos. Tienden a competir incluso con la pareja, a convertir cualquier desacuerdo en una batalla por imponer su voluntad, y a aburrirse cuando la relacion pierde la emocion del principio. El desarrollo pasa por aprender que la verdadera union no requiere la disolucion del yo individual, y que la cooperacion no es una forma de derrota.

En su expresion mas positiva, los nativos con esta posicion son personas que aportan una energia revitalizante a sus relaciones. Su honestidad radical y su disposicion a encarar los conflictos de frente evitan que los problemas se pudran en silencio. Son parejas que defienden a quienes aman con una lealtad feroz y que inspiran con su valentia para ser autenticos. La sombra a trabajar es la impaciencia y la tendencia a tratar la relacion como una conquista que, una vez lograda, pierde su interes.""" ,

    "casa_7_tauro": """Casa 7 en Tauro

Quienes tienen la Casa 7 en Tauro buscan en las relaciones la estabilidad, la lealtad y la seguridad que este signo de tierra valora por encima de todo. No les interesan las relaciones pasajeras ni los vinculos superficiales: ellos quieren construir algo que perdure, algo solido en lo que puedan confiar. La pareja es un refugio, un espacio donde encontrar la paz y la certeza de que hay alguien que estara ahi pase lo que pase. Su forma de amar es constante, sensorial y profundamente leal, y demuestran su afecto a traves de actos concretos de cuidado y presencia.

La imagen que proyectan en la pareja es la de alguien confiable, paciente y devoto que ofrece una estabilidad que pocos pueden igualar. Los demas las perciben como personas en las que se puede confiar ciegamente, que no abandonan cuando las cosas se ponen dificiles y que construyen relaciones sobre bases solidas. Sin embargo, detras de esa fachada de roca hay una resistencia al cambio que puede convertir la relacion en una prision de rutina y previsibilidad.

El conflicto interno de esta posicion es la posesividad y el miedo a perder lo que han construido. Estas personas pueden aferrarse a relaciones que ya no funcionan simplemente porque no soportan la idea de perder la seguridad que representan. Los celos y la necesidad de control pueden aparecer cuando sienten que la estabilidad de la relacion esta amenazada. Su terquedad las lleva a enquistarse en conflictos que requieren flexibilidad, y su resistencia al cambio puede sofocar el crecimiento de la pareja y el propio. El desarrollo pasa por aprender que la verdadera seguridad en el amor no viene del control sino de la confianza, y que a veces soltar es la forma mas profunda de cuidado.

En su expresion mas positiva, los nativos con esta posicion son las parejas mas leales y dedicadas que existen. Su amor es constante, presente y se demuestra en los pequenos gestos cotidianos que construyen una vida compartida. Son quienes estan ahi en las buenas y en las malas, quienes cumplen sus promesas y quienes convierten el hogar en un verdadero refugio. La sombra a trabajar es la posesividad y la tendencia a quedarse en relaciones por miedo a la soledad o al cambio.""" ,

    "casa_7_geminis": """Casa 7 en Geminis

Quienes tienen la Casa 7 en Geminis se acercan a las relaciones desde la curiosidad intelectual y la necesidad de estimulo mental constante. Para ellos, la pareja es antes que nada una conversacion que nunca termina, un intercambio de ideas, de perspectivas y de palabras que los mantiene mentalmente vivos. Necesitan a alguien con quien puedan hablar de todo, alguien que los sorprenda con nuevas ideas y que no los confine a la monotonia de la rutina. La variedad y la novedad son tan importantes como el afecto, y una relacion que deja de estimular su mente se convierte rapidamente en una relacion que deja de interesarles.

La imagen que proyectan en la pareja es la de alguien divertido, inteligente y socialmente habilidoso que sabe como mantener viva la chispa de la conversacion. Los demas las perciben como personas fascinantes y entretenidas, capaces de adaptarse a cualquier situacion social y de conectar con cualquier persona. Sin embargo, detras de esa fachada de encanto y versatilidad hay una dificultad para comprometerse y una tendencia a huir de la profundidad emocional que asusta.

El conflicto interno de esta posicion es la dispersion y el miedo a la intimidad profunda. Estas personas pueden saltar de una relacion a otra o mantener multiples vinculos simultaneos porque el compromiso con una sola persona les parece una limitacion a su libertad. Su tendencia a intelectualizar las emociones las lleva a analizar la relacion en lugar de vivirla, a convertir los sentimientos en temas de conversacion en lugar de experiencias que se sienten. El desarrollo pasa por aprender que la verdadera conexion requiere momentos de silencio compartido, de presencia sin palabras, y que la intimidad emocional es un territorio que no se puede explorar solo con la mente.

En su expresion mas positiva, los nativos con esta posicion son parejas que nunca dejan de sorprender y de crecer. Su capacidad de comunicacion y su mente abierta hacen de la relacion un espacio de aprendizaje mutuo y de exploracion constante. Son expertos en mantener la relacion fresca y en encontrar nuevas formas de conectar. La sombra a trabajar es la superficialidad emocional y la tendencia a evadir los compromisos que requieren profundidad.""" ,

    "casa_7_cancer": """Casa 7 en Cancer

Quienes tienen la Casa 7 en Cancer se entregan a las relaciones con una profundidad emocional que pocos pueden comprender. Para ellos, la pareja no es solo una compania: es un hogar, un refugio emocional donde encontrar la seguridad que el mundo exterior no ofrece. Aman desde un lugar de cuidado, de proteccion, de una ternura que busca nutrir al otro como si fuera parte de si mismos. Cada gesto de amor es una forma de decir "estoy aqui, no temas, yo te cuido", y su conexion con la pareja es tan visceral que a veces pierden la distincion entre sus propias emociones y las del ser amado.

La imagen que proyectan en la pareja es la de alguien dulce, sensible y profundamente dedicado que convierte la relacion en un espacio de cuidado mutuo. Los demas las perciben como personas que aman de verdad, que estan dispuestas a darlo todo por quienes quieren y que crean un vinculo de lealtad incondicional. Sin embargo, detras de esa fachada de entrega hay una dependencia emocional que puede volverse asfixiante tanto para ellas como para la pareja.

El conflicto interno de esta posicion es la fusion emocional y el miedo al abandono. Estas personas pueden perder su propia identidad dentro de la relacion, absorbiendo los estados de animo y las necesidades del otro hasta no saber donde terminan ellas y donde empieza la pareja. Su necesidad de seguridad las lleva a veces a conductas de control emocional, a manipular a traves del cuidado, a generar dependencia en el otro para asegurarse de que no se ira. El desarrollo pasa por aprender que el amor verdadero incluye la autonomia, que cuidar del otro no significa sacrificarse, y que la seguridad en el vinculo viene de la confianza y no del control.

En su expresion mas positiva, los nativos con esta posicion son las parejas mas nutritivas y protectoras que existen. Su capacidad de empatia y su sensibilidad emocional crean un espacio de seguridad donde la pareja puede ser vulnerable sin miedo. Aman con una ternura que sana, con una presencia que reconforta, y su lealtad es tan profunda como el oceano. La sombra a trabajar es la dependencia emocional y la tendencia a perderse en el otro.""" ,

    "casa_7_leo": """Casa 7 en Leo

Quienes tienen la Casa 7 en Leo se acercan a las relaciones con la generosidad y el drama del corazon solar que rige este signo. Para ellos, la pareja es un escenario donde el amor se celebra, donde la vida se vive con pasion y donde ambos pueden brillar sin temor a opacar al otro. Aman con una intensidad que busca ser correspondida no solo en sentimiento sino en reconocimiento: necesitan ser vistos, valorados y admirados por quien han elegido como companero. La relacion debe ser especial, unica, digna de ser contada como una gran historia de amor.

La imagen que proyectan en la pareja es la de alguien generoso, calido y apasionado que convierte la relacion en una celebracion continua. Los demas las perciben como personas que aman intensamente, que se entregan con todo su ser y que hacen sentir a su pareja que es la persona mas especial del universo. Sin embargo, detras de esa fachada de generosidad radiante hay una necesidad de atencion que puede volarse exigente y un orgullo que dificulta la resolucion de conflictos.

El conflicto interno de esta posicion es el ego y la necesidad de ser el centro de la atencion incluso dentro de la relacion. Estas personas pueden competir con la pareja por el protagonismo, sentirse heridas cuando no reciben la admiracion que esperan, y tener dificultades para compartir el escenario de la vida. Su orgullo les impide pedir perdon o mostrar vulnerabilidad, y su necesidad de ser especiales puede llevarlas a buscar atencion fuera de la relacion si no se sienten suficientemente valoradas. El desarrollo pasa por aprender que el amor verdadero no necesita un publico para ser valioso, y que la generosidad mas profunda es la que permite al otro brillar sin sentirse amenazado.

En su expresion mas positiva, los nativos con esta posicion son parejas que celebran el amor con una alegria contagiosa y una generosidad que inspira. Su capacidad de hacer sentir especial a la pareja, de organizar momentos inolvidables y de infundir pasion en la vida cotidiana convierte la relacion en una aventura compartida. La sombra a trabajar es el egoismo y la necesidad constante de validacion.""" ,

    "casa_7_virgo": """Casa 7 en Virgo

Quienes tienen la Casa 7 en Virgo se acercan a las relaciones con la mente analitica y el corazon servicial de este signo de tierra. Para ellos, la pareja es un proyecto que merece atencion, cuidado y mejora continua. Aman a traves del servicio: demostrando su afecto con acciones concretas, con atencion a los detalles, con una presencia que anticipa las necesidades del otro. Su amor no es grandioso ni dramatico, sino que se expresa en los pequenos gestos cotidianos, en la memoria de lo que la pareja necesita, en la disposicion constante a ayudar y a mejorar la vida compartida.

La imagen que proyectan en la pareja es la de alguien dedicado, atento y confiable que siempre esta dispuesto a hacer la vida del otro mas facil. Los demas las perciben como parejas responsables y cuidadosas que ponen el bienestar de la relacion por encima de sus propias necesidades. Sin embargo, detras de esa fachada de servicio hay una tendencia a la critica y una exigencia perfeccionista que puede desgastar el vinculo.

El conflicto interno de esta posicion es la critica constante y la dificultad para aceptar la imperfeccion en la pareja. Estas personas pueden analizar tanto la relacion que pierden la capacidad de disfrutarla, encontrando siempre algo que mejorar, algo que corregir, algo que no esta a la altura de sus estandares. Su tendencia a preocuparse por los detalles puede convertirse en ansiedad que contamina la espontaneidad del amor. Pueden elegir parejas a quienes "arreglar" o "salvar", repitiendo una dinamica de cuidador y cuidado que las deja agotadas. El desarrollo pasa por aprender que el amor no es un problema que resolver sino una experiencia que vivir, y que la perfeccion no es el objetivo de una relacion sana.

En su expresion mas positiva, los nativos con esta posicion son parejas excepcionalmente dedicadas que construyen relaciones solidas a traves del servicio y la atencion constante. Su capacidad de notar los detalles, de recordar lo que importa y de estar presentes en los momentos dificiles las convierte en companeras invaluables. La sombra a trabajar es la critica excesiva y la tendencia a querer perfeccionar a la pareja en lugar de aceptarla.""" ,

    "casa_7_libra": """Casa 7 en Libra

Quienes tienen la Casa 7 en Libra son los diplomaticos natos del amor, aquellos para quienes la pareja no es solo una opcion sino una necesidad casi existencial. Libra rige naturalmente la Casa 7, y esta posicion otorga una comprension innata de la dinamica de las relaciones, del arte de la negociacion y de la busqueda del equilibrio en el vinculo. Para ellos, la relacion es el espejo donde se reflejan, el espacio donde encuentran su complemento y donde la vida adquiere su verdadero significado. No conciben la existencia plena sin un companero con quien compartirla, y esta busqueda de la media naranja puede convertirse en el eje central de su vida.

La imagen que proyectan en la pareja es la de alguien encantador, elegante y diplomatico que sabe como mantener la armonia y como hacer sentir especial a quien esta a su lado. Los demas las perciben como personas que nacieron para estar en pareja, que tienen un talento natural para crear relaciones armoniosas y que saben navegar los conflictos con gracia. Sin embargo, detras de esa fachada de equilibrio hay una indecision paralizante y un miedo al conflicto que puede llevar al sacrificio de la autenticidad.

El conflicto interno de esta posicion es la dependencia de la pareja para sentirse completos y la dificultad para estar solos. Estas personas pueden sacrificar sus propias necesidades, opiniones y deseos con tal de mantener la paz y la armonia en la relacion. Su miedo a la confrontacion las lleva a evitar conversaciones dificiles, a posponer conflictos necesarios y a acumular resentimientos que terminan estallando cuando ya no pueden mas. La indecision se manifiesta en la dificultad para comprometerse o para terminar relaciones que ya no funcionan. El desarrollo pasa por aprender que la armonia verdadera no es la ausencia de conflicto sino la capacidad de atravesarlo juntos, y que una relacion sana requiere dos individuos completos, no dos mitades que se buscan mutuamente.

En su expresion mas positiva, los nativos con esta posicion tienen un talento extraordinario para crear relaciones armoniosas y equilibradas. Su capacidad de negociacion, su sensibilidad estetica y su deseo genuino de justicia las convierte en parejas que saben construir vinculos de respeto mutuo y colaboracion. La sombra a trabajar es la dependencia emocional y la tendencia a sacrificar la propia identidad por mantener la paz.""" ,

    "casa_7_escorpio": """Casa 7 en Escorpio

Quienes tienen la Casa 7 en Escorpio se sumergen en las relaciones con una intensidad que puede resultar abrumadora y transformadora a partes iguales. Para ellos, la pareja no es un complemento agradable ni una compania para los momentos de ocio: es un abismo donde estan dispuestos a caer, un territorio de exploracion profunda donde las mascaras caen y las almas se desnudan. Aman con una pasion que no conoce termino medio, con una entrega total que exige del otro la misma honestidad radical y la misma disposicion a mirar sin miedo las sombras propias y ajenas.

La imagen que proyectan en la pareja es la de alguien magnetico, intenso y misterioso que atrae con una fuerza que otros no pueden explicar. Los demas las perciben como personas que aman con una profundidad que pocos estan dispuestos a igualar, y que tienen una capacidad de lealtad y de compromiso que raya en lo absoluto. Sin embargo, detras de esa fachada de poder magnetico hay un miedo profundo a la traicion y una desconfianza que puede envenenar la relacion desde dentro.

El conflicto interno de esta posicion es la desconfianza y la necesidad de control emocional. Estas personas pueden entrar en relaciones con una intensidad que asfixia, exigiendo del otro una transparencia total mientras ellas mismas guardan secretos como forma de proteccion. Su miedo a la vulnerabilidad las lleva a probar a la pareja, a buscar sus puntos debiles, a asegurarse de que no seran traicionadas. Los celos y la posesividad pueden convertirse en herramientas de control que destruyen precisamente lo que quieren proteger. El desarrollo pasa por aprender que la confianza es un salto que no se puede controlar, que la vulnerabilidad no es debilidad sino la puerta a la verdadera intimidad, y que el poder en el amor no esta en controlar al otro sino en entregarse sin reservas.

En su expresion mas positiva, los nativos con esta posicion tienen una capacidad de amar que transforma todo lo que toca. Su lealtad es absoluta, su pasion es sanadora y su disposicion a atravesar las crisis junto a la pareja crea vinculos que resisten cualquier tormenta. La sombra a trabajar es la desconfianza y la tendencia a manipular emocionalmente para sentirse seguros.""" ,

    "casa_7_sagitario": """Casa 7 en Sagitario

Quienes tienen la Casa 7 en Sagitario se acercan a las relaciones con el espiritu aventurero y la sed de horizonte que caracteriza a este signo de fuego. Para ellos, la pareja debe ser una companera de viaje, alguien con quien explorar el mundo y expandir los limites de lo conocido. No les interesan las relaciones que las confinan ni los vinculos que las atan a una rutina predecible: necesitan espacio para crecer, para viajar, para perseguir sus ideales, y buscan a alguien que no solo lo entienda sino que se sume a la aventura con entusiasmo.

La imagen que proyectan en la pareja es la de alguien optimista, entusiasta y libre que inspira con su amor por la vida y su confianza en el futuro. Los demas las perciben como personas que aportan alegria y expansion a la relacion, que nunca dejan que la monotonia se instale y que ven siempre el lado positivo de las dificultades. Sin embargo, detras de esa fachada de optimismo aventurero hay un miedo al compromiso y una tendencia a huir cuando la relacion exige profundidad.

El conflicto interno de esta posicion es el miedo a sentirse atrapado y la dificultad para comprometerse con una sola persona. Estas personas pueden evitar las relaciones serias o sabotearlas cuando se vuelven demasiado intimas, porque la cercania les parece una amenaza a su libertad. Su franqueza, que es una de sus mayores virtudes, puede convertirse en falta de tacto que hiere a la pareja. Tienden a idealizar relaciones a distancia o imposibles, donde el compromiso real no es necesario, y a aburrirse cuando la relation entra en la fase de la rutina y la construccion cotidiana. El desarrollo pasa por aprender que la verdadera libertad incluye la capacidad de comprometerse sin sentirse atrapado, y que la aventura mas profunda puede ser la de construir una vida compartida.

En su expresion mas positiva, los nativos con esta posicion son parejas que inspiran, que expanden los horizontes del otro y que nunca dejan que la relacion se vuelva estancada. Su optimismo es contagioso, su generosidad es genuina y su capacidad de ver el futuro con esperanza ilumina la vida compartida. La sombra a trabajar es la evasion del compromiso y la tendencia a buscar la libertad a costa de la intimidad.""" ,

    "casa_7_capricornio": """Casa 7 en Capricornio

Quienes tienen la Casa 7 en Capricornio se toman las relaciones con la misma seriedad y sentido de responsabilidad con que abordan el resto de su vida. Para ellos, la pareja no es un juego ni una aventura pasajera: es un compromiso que requiere dedicacion, madurez y la voluntad de construir algo que perdure en el tiempo. Aman con responsabilidad, con una conciencia del peso de las promesas y de la importancia de la lealtad a largo plazo. No se entregan facilmente, pero cuando lo hacen, es para siempre, y esperan del otro la misma seriedad y el mismo respeto por el vinculo que ellos ofrecen.

La imagen que proyectan en la pareja es la de alguien serio, confiable y maduro que ofrece una estabilidad emocional y material que pocos pueden igualar. Los demas las perciben como personas en las que se puede confiar para construir un futuro solido, que entienden el valor del compromiso y que no abandonan cuando las cosas se ponen dificiles. Sin embargo, detras de esa fachada de solidez hay una dificultad para mostrar vulnerabilidad y una tendencia a la frialdad emocional que puede distanciar a la pareja.

El conflicto interno de esta posicion es la rigidez y el miedo a la vulnerabilidad emocional. Estas personas pueden tratar la relacion como un proyecto mas que gestionar, midiendo el exito en terminos de logros y metas mas que en calidad de conexion emocional. Su tendencia a reprimir sus sentimientos y a priorizar la responsabilidad sobre la expresion del amor puede hacer que la pareja se sienta no amada o no valorada. Pueden elegir parejas por su estatus social o su capacidad de contribuir a sus metas, confundiendo la compatibilidad practica con el amor verdadero. El desarrollo pasa por aprender que la solidez de una relacion no depende solo de la responsabilidad sino de la capacidad de compartir la vulnerabilidad, y que el amor requiere tanto estructura como corazon.

En su expresion mas positiva, los nativos con esta posicion construyen relaciones que son verdaderas instituciones de amor y respeto mutuo. Su lealtad es inquebrantable, su sentido del compromiso es ejemplar y su capacidad de construir un futuro juntos es extraordinaria. La sombra a trabajar es la frialdad emocional y la tendencia a priorizar las apariencias sobre la autenticidad del vinculo.""" ,

    "casa_7_acuario": """Casa 7 en Acuario

Quienes tienen la Casa 7 en Acuario se acercan a las relaciones desde una perspectiva unica y poco convencional que desafia las expectativas sociales tradicionales. Para ellos, la pareja no es una posesion ni una fuente de seguridad emocional sino un companero en el camino de la vida con quien compartir ideales, proyectos y una vision del mundo. Necesitan espacio para ser quienes son, libertad para mantener su individualidad y una relacion que se base en la amistad y el respeto mutuo mas que en las demandas emocionales convencionales. El amor para ellos es antes que nada una conexion mental, un encuentro de mentes que piensan parecido y que miran el mundo desde una perspectiva compartida.

La imagen que proyectan en la pareja es la de alguien original, independiente intelectualmente y emocionalmente desapegado que ofrece una relacion basada en la libertad y el respeto mutuo. Los demas las perciben como personas que no se dejan atrapar por los celos ni por las demandas emocionales, y que valoran la autenticidad por encima de las convenciones sociales. Sin embargo, detras de esa fachada de independencia y originalidad hay una dificultad para conectar emocionalmente que puede dejar a la pareja sintiendose no amada.

El conflicto interno de esta posicion es la desconexion emocional y el miedo a la intimidad personal. Estas personas pueden sentirse mas comodas en relaciones no convencionales, a distancia o abiertas, porque la intimidad emocional profunda les resulta amenazante. Su tendencia a intelectualizar los sentimientos y a analizar la relacion en lugar de vivirla puede crear una distancia que la pareja siente como frialdad o desinteres. Pueden idealizar tanto la independencia que confunden el compromiso con la perdida de libertad. El desarrollo pasa por aprender que la intimidad emocional no es una amenaza a la individualidad sino una oportunidad de crecimiento compartido, y que el amor verdadero incluye la capacidad de estar presente emocionalmente sin perder la propia identidad.

En su expresion mas positiva, los nativos con esta posicion ofrecen relaciones basadas en la autenticidad, la libertad y el respeto mutuo. Son parejas que no intentan poseer ni controlar, que apoyan la individualidad del otro y que construyen vinculos desde la amistad y los ideales compartidos. La sombra a trabajar es la distancia emocional y la tendencia a priorizar la independencia sobre la conexion.""" ,

    "casa_7_piscis": """Casa 7 en Piscis

Quienes tienen la Casa 7 en Piscis se entregan a las relaciones con una sensibilidad que trasciende lo racional y con una capacidad de amar que disuelve los limites entre el yo y el otro. Para ellos, la pareja es una experiencia de fusion, de conexion espiritual, de encuentro de almas que va mas alla de lo que las palabras pueden expresar. Aman sin condiciones, sin juicios, con una compasion que todo lo comprende y que todo lo perdona. Su corazon esta abierto a la experiencia del amor en su forma mas pura, mas universal, mas conectada con el oceano de la conciencia donde todas las almas son una.

La imagen que proyectan en la pareja es la de alguien sonador, sensible y profundamente compasivo que ofrece un amor incondicional y una comprension que trasciende las palabras. Los demas las perciben como personas que aman con una entrega total, que son capaces de ver la belleza incluso en los defectos de la pareja y que ofrecen un refugio de aceptacion incondicional. Sin embargo, detras de esa fachada de amor incondicional hay una confusion de limites y una tendencia al sacrificio que puede llevar a la perdida de si mismas.

El conflicto interno de esta posicion es la dificultad para establecer limites y la tendencia a idealizar o a victimizarse en la relacion. Estas personas pueden perderse dentro de la pareja hasta no saber donde terminan ellas y donde empieza el otro, absorbiendo las emociones, los problemas y las cargas del ser amado como si fueran propios. Su tendencia a idealizar a la pareja las lleva a decepcionarse cuando la realidad no coincide con la fantasia, y su compasion puede convertirse en codependencia donde confunden el amor con el sacrificio y la entrega con la perdida de si mismas. El desarrollo pasa por aprender que el amor verdadero incluye el amor propio, que los limites no son barreras al amor sino estructuras que lo protegen, y que la union mas profunda requiere dos individuos enteros que eligen compartir su plenitud.

En su expresion mas positiva, los nativos con esta posicion ofrecen un amor que verdaderamente no conoce condiciones ni juicios. Su capacidad de compasion, de perdon y de conexion espiritual crea relaciones que sanan y que trascienden lo ordinario. La sombra a trabajar es el sacrificio excesivo y la tendencia a perderse en la pareja.""" ,
}

with open(FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

for key, value in ENTRIES.items():
    data[key] = value

with open(FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n=== CASA 7 — CHARACTER COUNTS ===\n")
total = 0
for key in sorted(ENTRIES.keys()):
    length = len(ENTRIES[key])
    sign = key.replace("casa_7_", "")
    status = "OK" if length >= 1800 else "FAIL"
    print(f"  {sign:20s}  {length:5d} chars  {status}")
    total += length

print(f"\n  {'TOTAL':20s}  {total:5d} chars")
print(f"  {'AVERAGE':20s}  {total//12:5d} chars")
print("\nDone. File updated successfully.")
