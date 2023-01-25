# weather-on-business-rating
This is an end-to-end data pipeline to see if the weather affects the rating of a restaurant.

Step:
1. Download data from this link:
Weather review -> (.json) https://email.app.bamboohr.com/c/eJyNkkFvozAQhX9NuVREGIPBBw7dKKTJbqpt2iZKL2hshuAEYxZMSPPrl2Rz2L2tZGmenp49n8fuhj6zqJsKLGYnbDtl6kzlySiz52izOg1nGu_SzfIXn8r0OS42q9SRfWeNTvBr6X1uw1LU6-XndMEWhx1dvctwoQa187mV87THj-q4OBj1cpDnl8tR_Zgu-92WVFdv7ZdEzFO7mKUM_Nn-dXtuxNuSO9Jo3ddKgr3TQB4GBZeeyxllLiGYu4KQwEUfQhpAUQiInTyRQeS0KFE19rqrMvsspJRTLBjkHheAELMY_KBgnIgCwQeXOuq_jn8IPGiaiQAtjCnbycjoWKyhvrW6KxaR6IbfQP119aXK72aVlNY23QN9evDTcQ3DMJGV0uPcJ3tzGh0NTefmYGHU19KhHVUDnXUHBFti615U40qT4y3mWhAVOm0ClyNM9mVfgSZ05NxrUNUfwORna_KxvN-feGz_-GS7x9k14pQJQcEwIFQAYzGVID1GOEcPQ6BxTEIHE8KicYQ8osTp_v4st1vrLGZTxuTpeHrl2_lBbzdcf2vW3zf_hisjocIEa_fj7Te-0NAI
Restaurant review -> (.csv)
https://email.app.bamboohr.com/c/eJyNUU1v4jAQ_TXkUgXFceLEhxxaRGjYpdrSNoheorEzJoZ8LXEI9NdvYDns3ipZmuen8XvPM93QZwartgSD2QmPnW7qTOfRCLPnIF2dhjMNt3G6_M1nMn4OVbqKLdl3pqkivCydz41fiHq9_JwlLNlv6epd-oke9NblRi7iHj_KQ7Jv9Mtenl--DvrnbNlvN6S8cmu3IGIRm2QeM3Dnu9fNuRVvS27Jpqr6Wksw9zSQ-57i0rE5o8wmBHNbEOLZ6IJPPVBKQGjlkfQC64gSdWuur8pml_mUcoqKQe5wAQghC8H1FONEKAQXbGrpb8lPPAfadiqgEk1THKdjRstgDfXN6o5YQIJb_Bbqy5WXOr-TZVQY03YT-jhx4_EMwzC9YNlehcZrDgY6NCOyjhF8HWC6K_oSKkJH410FuvzrGP06NvlY3u87G_UeHk33ML-2WEWkBDqeHzDFPJ-5yAKVh6BcD4RLfImOhRFhwTgTHlBidf9u__aNKgvZjDF5Opxe-WaxrzYpr57a9Y_0_-aykVBihLX98fYH2pS_Dg

2. Convert Data with python 
3. Ingest data with Airflow
4. run sql code to find relation between weather and restaurant rating
5. Create data visualizations to see the results more clearly
