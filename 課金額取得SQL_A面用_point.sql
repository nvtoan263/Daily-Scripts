select lp.charge_object_id, ta.*, ti.day_class_id, ti.time_class_id, CAST(ab.start_time AS INT) start_time, CAST(ab.end_time AS INT) end_time, lo.location_class_id   
from erp_tariff_class_A ta, time_classes_A ti, location_classes_A lo, location_point_A lp, absolute_time_of_day_A ab
where CAST(ta.tariff_class_id AS INT) = CAST(ti.tariff_class_id AS INT)   
and CAST(ta.tariff_class_id AS INT) = CAST(lo.tariff_class_id AS INT)   
and CAST(ta.table_type AS INT) = 148   
and CAST(ti.table_type AS INT) = 148   
and CAST(lo.table_type AS INT) = 148   
and CAST(lo.location_class_id AS INT) = CAST(lp.location_class AS INT)
and CAST(ti.time_class_id AS INT) = CAST(ab.time_class_id AS INT)
and CAST(ab.table_type AS INT) = 136
and (  
	(
		(
			CAST(ti.day_class_id AS INT) in (
				select CAST(ne.time_class_id AS INT)   
				from nominal_elements_A ne, SELECT_DATA sd   
				where CAST(ne.table_type AS INT) = 134   
				and CAST(ne.date AS INT) = CAST(strftime('%Y%m%d', sd.YYYYMMDD) AS INT)  
				and CAST(ne.time_class_id AS INT) <> 0
			)   
			or 0 in (
				select CAST(ne.time_class_id AS INT)   
				from nominal_elements_A ne, SELECT_DATA sd   
				where CAST(ne.table_type AS INT) = 134   
				and CAST(ne.date AS INT) = CAST(strftime('%Y%m%d', sd.YYYYMMDD) AS INT)
			)
		)   
	)  
	or (
		(
			CAST(ti.day_class_id AS INT) in (
				select CAST(ne.time_class_id AS INT)   
				from nominal_elements_A ne, SELECT_DATA sd   
				where CAST(ne.table_type AS INT) = 134   
				and CAST(ne.date AS INT) = (
					select CAST(strftime('%Y%m%d', sd.YYYYMMDD, 'days') AS INT)
				)   
				and CAST(ne.time_class_id AS INT) <> 0
			)   
			or 0 in (
				select CAST(ne.time_class_id AS INT)   
				from nominal_elements_A ne, SELECT_DATA sd   
				where CAST(ne.table_type AS INT) = 134   
				and CAST(ne.date AS INT) = (
					select CAST(strftime('%Y%m%d', sd.YYYYMMDD, 'days') AS INT)
				)
			)
		)   
	)  
)  
and CAST(lp.charge_object_id AS INT) in (
	select CAST(ChargeObjectID AS INT)
	from SELECT_DATA
)
order by start_time, end_time, ti.time_class_id;
