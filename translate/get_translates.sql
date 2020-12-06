SELECT main_translate.value AS translate, main_subject.value AS subject
	FROM main_translate 
	LEFT JOIN main_subject ON main_translate.subject_id = main_subject.id
	WHERE entry_id = (
		SELECT id FROM main_entry WHERE origin = "bring" AND lang_key = "ru_en"
	)