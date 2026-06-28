from django.shortcuts import render, redirect
import datetime

# --- E1 - CHOIX DE L'OPERATION ---
def e1_choix_operation_view(request):
    if request.method == 'POST':
        request.session['operation'] = request.POST.get('operation')
        return redirect('selection_crypto')
    return render(request, 'kiosk/e1_choix_operation.html')


# --- E2 - SELECTION DE LA CRYPTO ---
def e2_selection_crypto_view(request):
    if request.method == 'POST':
        request.session['crypto'] = request.POST.get('crypto')
        return redirect('selection_montant')
    return render(request, 'kiosk/e2_selection_crypto.html')


# --- E3 - SELECTION DU MONTANT & VARIANTES ---
def e3_selection_montant_view(request):
    if request.method == 'POST':
        request.session['montant'] = request.POST.get('montant')
        return redirect('conditions')
    return render(request, 'kiosk/e3_selection_montant.html')

def e3_autre_montant_view(request):
    if request.method == 'POST':
        request.session['montant'] = request.POST.get('montant', 100)
        return redirect('conditions')
    return render(request, 'kiosk/e3_autre_montant.html')

def e3_conditions_view(request):
    if request.method == 'POST':
        return redirect('verif_telephone')
    return render(request, 'kiosk/e3_conditions.html')


# --- E4 - VERIFICATION DES COORDONNEES ---
def e4_verif_telephone_view(request):
    if request.method == 'POST':
        request.session['telephone'] = request.POST.get('telephone')
        return redirect('verif_email')
    return render(request, 'kiosk/e4_verif_telephone.html')

def e4_verif_email_view(request):
    if request.method == 'POST':
        request.session['email'] = request.POST.get('email')
        return redirect('kyc_photo')
    return render(request, 'kiosk/e4_verif_email.html')


# --- E5 - VERIFICATION D'IDENTITE (KYC) ---
def e5_kyc_photo_view(request):
    if request.method == 'POST':
        return redirect('kyc_verifier')
    return render(request, 'kiosk/e5_kyc_photo.html')

def e5_kyc_verifier_view(request):
    # Correspond à l'image f8_2.png ("Vérifier votre identité... Un instant, s'il vous plaît")
    # Redirection automatique via JavaScript dans le template vers 'customer_details'
    return render(request, 'kiosk/e5_kyc_verifier.html')

def e51_customer_details_view(request):
    # Correspond aux images f10_2.png et f11_2.png (Situation, Revenu, Origine des fonds)
    if request.method == 'POST':
        request.session['situation_pro'] = request.POST.get('situation_pro')
        request.session['revenu_mensuel'] = request.POST.get('revenu_mensuel')
        # Origine des fonds peut être multiple (checkboxes)
        request.session['origine_fonds'] = request.POST.getlist('origine_fonds')
        
        return redirect('customer_details_v2')
    return render(request, 'kiosk/e51_customer_details.html')

def e51_customer_details_v2_view(request):
    # Écran de succès vert/validation avant le choix du wallet
    return render(request, 'kiosk/e51_customer_details_v2.html')


# --- E6 - PORTEFEUILLE CLIENT ---
def e6_choix_wallet_view(request):
    if request.method == 'POST':
        request.session['choix_wallet'] = request.POST.get('choix_wallet')
        return redirect('recapitulatif')
    return render(request, 'kiosk/e6_choix_wallet.html')


# --- E7 - RECAPITULATIF DE LA TRANSACTION ---
def e7_recapitulatif_view(request):
    if request.method == 'POST':
        return redirect('scan_wallet')
    return render(request, 'kiosk/e7_recapitulatif.html')

def e7_recapitulatif_details_view(request):
    if request.method == 'POST':
        return redirect('scan_wallet')
    return render(request, 'kiosk/e7_recapitulatif_details.html')


# --- E8 à E11 - SCAN, ENCAISSEMENT ET TRAITEMENT ---
def e8_scan_wallet_view(request):
    # Redirection automatique vers le dépôt après scan simulé en JS
    return render(request, 'kiosk/e8_scan_wallet.html')

def e9_insertion_especes_view(request):
    if request.method == 'POST':
        # Récupère la valeur saisie ou injectée via les boutons du template
        request.session['montant_final'] = request.POST.get('montant', 100)
        return redirect('traitement')
    return render(request, 'kiosk/e9_insertion_especes.html')

def e10_traitement_view(request):
    # Écran d'attente blockchain (géré en JS vers la page finale)
    return render(request, 'kiosk/e10_traitement.html')

def e11_fin_transaction_view(request):
    # Correspond à l'image f18_2.png
    if request.method == 'POST' and 'imprimer' in request.POST:
        # Ici, l'utilisateur a cliqué sur "Imprimer le reçu"
        # On passe un indicateur au template pour déclencher window.print() en JS
        context = {
            'declencher_impression': True,
            'montant_insere': request.session.get('montant_final', '100,00 €'),
            'btc_envoye': '0.00237 BTC',
            'frais': '0.0005 BTC',
            'adresse_reception': 'bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kygt08',
            'ref_blockchain': '0x3f1b8a9c4e2d9b7a8c5f3e6b1d2a7c8f4b9e1f2c3d4a5b6c7e8f9a0b1c2d3e4f',
            'date_heure': '2025-06-16T18:42:30Z' # Format exact f18_2.png
        }
        # Optionnel : Vider la session après l'impression pour sécuriser la borne pour le client suivant
        # request.session.flush() 
        return render(request, 'kiosk/e11_fin_transaction.html', context)

    # Affichage normal initial de l'écran 11
    context = {
        'declencher_impression': False,
        'montant_insere': request.session.get('montant_final', '100,00 €'),
        'btc_envoye': '0.00237 BTC',
        'frais': '0.0005 BTC',
        'adresse_reception': 'bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kygt08',
        'ref_blockchain': '0x3f1b8a9c4e2d9b7a8c5f3e6b1d2a7c8f4b9e1f2c3d4a5b6c7e8f9a0b1c2d3e4f',
        'date_heure': '2025-06-16T18:42:30Z'
    }
    return render(request, 'kiosk/e11_fin_transaction.html', context)



