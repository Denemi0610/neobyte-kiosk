from django.urls import path
from . import views

urlpatterns = [
    # E1 à E3
    path('', views.e1_choix_operation_view, name='choix_operation'),
    path('selection-crypto/', views.e2_selection_crypto_view, name='selection_crypto'),
    path('selection-montant/', views.e3_selection_montant_view, name='selection_montant'),
    path('autre-montant/', views.e3_autre_montant_view, name='autre_montant'),
    path('conditions/', views.e3_conditions_view, name='conditions'),
    
    # E4 (Coordonnées)
    path('verification-telephone/', views.e4_verif_telephone_view, name='verif_telephone'),
    path('verification-email/', views.e4_verif_email_view, name='verif_email'),
    
    # E5 & E5.1 (KYC)
    path('kyc-photo/', views.e5_kyc_photo_view, name='kyc_photo'),
    path('kyc-verifier/', views.e5_kyc_verifier_view, name='kyc_verifier'),
    path('customer-details/', views.e51_customer_details_view, name='customer_details'),
    path('customer-details-v2/', views.e51_customer_details_v2_view, name='customer_details_v2'),
    
    # E6 à E11
    path('choix-wallet/', views.e6_choix_wallet_view, name='choix_wallet'),
    path('recapitulatif/', views.e7_recapitulatif_view, name='recapitulatif'),
    path('recapitulatif-details/', views.e7_recapitulatif_details_view, name='recapitulatif_details'),
    path('scan-wallet/', views.e8_scan_wallet_view, name='scan_wallet'),
    path('insertion-especes/', views.e9_insertion_especes_view, name='insertion_especes'),
    path('traitement/', views.e10_traitement_view, name='traitement'),
    path('fin-transaction/', views.e11_fin_transaction_view, name='fin_transaction'),
]