-- tragic historic actives
select b.region, b.vanid,
sum(case when b.event_date>='2017-07-14' and b.event_date<='2017-08-13' then 1 else null end) as Week_3,
sum(case when b.event_date>='2017-07-21' and b.event_date<='2017-08-20' then 1 else null end) as Week_4,
sum(case when b.event_date>='2017-07-28' and b.event_date<='2017-08-27' then 1 else null end) as Week_5,
sum(case when b.event_date>='2017-08-04' and b.event_date<='2017-09-03' then 1 else null end) as Week_6,
sum(case when b.event_date>='2017-08-11' and b.event_date<='2017-09-10' then 1 else null end) as Week_7,
sum(case when b.event_date>='2017-08-18' and b.event_date<='2017-09-17' then 1 else null end) as Week_8,
sum(case when b.event_date>='2017-08-25' and b.event_date<='2017-09-24' then 1 else null end) as Week_9,
sum(case when b.event_date>='2017-09-01' and b.event_date<='2017-10-01' then 1 else null end) as Week_10,
sum(case when b.event_date>='2017-09-08' and b.event_date<='2017-10-08' then 1 else null end) as Week_11,
sum(case when b.event_date>='2017-09-15' and b.event_date<='2017-10-15' then 1 else null end) as Week_12,
sum(case when b.event_date>='2017-09-22' and b.event_date<='2017-10-22' then 1 else null end) as Week_13,
sum(case when b.event_date>='2017-09-29' and b.event_date<='2017-10-29' then 1 else null end) as Week_14,
sum(case when b.event_date>='2017-10-06' and b.event_date<='2017-11-05' then 1 else null end) as Week_15,
sum(case when b.event_date>='2017-10-13' and b.event_date<='2017-11-12' then 1 else null end) as Week_16,
sum(case when b.event_date>='2017-10-20' and b.event_date<='2017-11-19' then 1 else null end) as Week_17,
sum(case when b.event_date>='2017-10-27' and b.event_date<='2017-11-26' then 1 else null end) as Week_18,
sum(case when b.event_date>='2017-11-03' and b.event_date<='2017-12-03' then 1 else null end) as Week_19,
sum(case when b.event_date>='2017-11-10' and b.event_date<='2017-12-10' then 1 else null end) as Week_20,
sum(case when b.event_date>='2017-11-17' and b.event_date<='2017-12-17' then 1 else null end) as Week_21,
sum(case when b.event_date>='2017-11-24' and b.event_date<='2017-12-24' then 1 else null end) as Week_22,
sum(case when b.event_date>='2017-12-01' and b.event_date<='2017-12-31' then 1 else null end) as Week_23,
sum(case when b.event_date>='2017-12-08' and b.event_date<='2018-01-07' then 1 else null end) as Week_24,
sum(case when b.event_date>='2017-12-15' and b.event_date<='2018-01-14' then 1 else null end) as Week_25,
sum(case when b.event_date>='2017-12-22' and b.event_date<='2018-01-21' then 1 else null end) as Week_26,
sum(case when b.event_date>='2017-12-29' and b.event_date<='2018-01-28' then 1 else null end) as Week_27,
sum(case when b.event_date>='2018-01-05' and b.event_date<='2018-02-04' then 1 else null end) as Week_28,
sum(case when b.event_date>='2018-01-12' and b.event_date<='2018-02-11' then 1 else null end) as Week_29,
sum(case when b.event_date>='2018-01-19' and b.event_date<='2018-02-18' then 1 else null end) as Week_30,
sum(case when b.event_date>='2018-01-26' and b.event_date<='2018-02-25' then 1 else null end) as Week_31,
sum(case when b.event_date>='2018-02-02' and b.event_date<='2018-03-04' then 1 else null end) as Week_32,
sum(case when b.event_date>='2018-02-09' and b.event_date<='2018-03-11' then 1 else null end) as Week_33,
sum(case when b.event_date>='2018-02-16' and b.event_date<='2018-03-18' then 1 else null end) as Week_34,
sum(case when b.event_date>='2018-02-23' and b.event_date<='2018-03-25' then 1 else null end) as Week_35
FROM
(select t1.region, a.vanid, a.event_date, t2.week from
(select t1.vanid, cast(left(t1.datetimeoffsetbegin,10) as date) as event_date from vansync_il_gov_2018.dnc_eventsignups T1
join vansync_il_gov_2018.dnc_eventsignupsstatuses T2 on t2.eventsignupid=t1.eventsignupid
where (
  t2.eventstatusid=2
  AND t2.eventsignupseventstatusid=t1.currenteventsignupseventstatusid
  AND (t1.eventroleid='191345' OR t1.eventroleid='186915' OR t1.eventroleid='186911')
)
) a
 JOIN public.actives T1 on t1.vanid=a.vanid
join public.weeks T2 on t2.date=a.event_date
order by 3) b
group by 1, 2
order by 3, 4, 1
