1- توصيف الحالة:
 نبدأ باختيار المرحلة التي نريدها من خلال مايدخله المستخدم
 بعد اختيار المرحلة نقوم بانشاء board جديد وهو class هذا الclass يقوم بانشاء الرقعة 
وكل خانة من هذه الرقعة هي عبارة عن cell و وهي عبارة عن class يحتوي هذا ال class على احداثيات كل خانة تحتوي ايضا علي attribute يدعى whitespace وهو قيمة بوليانية مسؤولة عن تحديد الخلايا الهدف(البيضاء)
ويوجد attribute اخر يدعى cell type وهو مسؤول عن تحديد نوع الخلية(قطع حديدية , مغناطيس موجب , مغناطيس سالب).
2- فضاء الحالات:
يتغير فضاء الحالات حسب موقع المغناطيس بحيث نقوم باستدعاء توابع الحركة وهي بدورها مسؤؤلة عن تغيير حالة الرقعة (سوف اقوم بشرح توابع الحركة في العمليات والاجرائيات)
يمكن الوصول لحالة غير قابلة للحل(وذلك عند انتهاء عدد ل lives وهو attribute  يوجد في class ال board  وهو مسؤول عن عدد الحركات المسموحة )
3-الحالة الابتدائية:
بعد توزيع الخلايا cells على الرقعة نقوم بتحديد نوع الخلايا وذلك عن طريق استدعاء دالة تقوم بتحديد ال cell type 
وايضا نقوم بتحديد ان كانت خلية بيضاء ام لا عن طريق تحديد ال whitespace.
4- العمليات والاجرائيات:
بعد تحديد نوع الخلايا نقوم الان باختيار الخلية التي تحتوي على مغناطيس لتحريكه الى خلية (موقع) جديدة
وبعد تحريك المغناطيس نقوم بفحص نوعه اذا كان من النوع الموجب نقوم باستدعاء الدالة المسؤولة عن تحريك القطع الحديدية باتجاهه 
واذا كان نوعه من النوع السالب نقوم باستدعاء الدالة المسؤولة عن تحريك القطع الحديدية بعيدا عنه.
5- الحالة النهائية:
وبعد عمليات التحريك نقوم بفحص وضع الرقعة بحيث ان كانت كل خلية بيضاء تحتوي على قطعة حديدية او مغناطيس اي انها غير فارغة 
ونقوم بذلك عن طريق attribute  يوجد في class  ال cell وهو whiteFilled وهي قيمة بوليانية تاخذ true ان كانت الخلية البيضاء تحتوي على قطعة حديدية او مغناطيس و تاخذ false ان كانت الخلية البيضاء فارغة.
خوارزمية ال DFS:
بنية التخزين stack , نقوم بالتحقق من الرقعة في الحالة الابتدائية ونفحص ان كانت حالة رابحة ام لا ان لم تكن:
نقوم بفحص ان كانت مزارة ام لا عن طريق تحويل الرقعة الى مصفوفة string ونقوم بالمقارنة
في حال كانت مزارة نقوم بتجاهل هذه الرقعة
وان لم تكن نقوم باضافة الرقعة الى set ال visited
في كل حالة يمكننا تحريك المغناطسي اليها نقوم بانشاء رقعة جديدة (state)
ناخد كل الحالات ونضعها في ال stack ناخد الرقعة التي تكون في اعلى ال stack ونفحصها وبعد عملية الفحص نقوم بوضع الحلات التي تنتج عن هذه الحالة ونفحص الرقعة التي في اعلى ال stack وهكذا...
ونقوم بالتراجع حتى الوصول الى حالة رابحة.
6-خوارزمية ال BFS:
بنية التخزين queue , بحث نقوم بفحص جميع الابناء قبل الانتقال الى العمق الجديد
وتحديد الخلايا المزارة وحالة الربح هي نفس مبدأ ال DFS.
