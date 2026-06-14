from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm
from .ai_service import get_health_prediction


def patient_list(request):

    patients = Patient.objects.all()

    return render(
        request,
        'patient/list.html',
        {'patients': patients}
    )


def patient_create(request):

    form = PatientForm(request.POST or None)

    if form.is_valid():

        patient = form.save(commit=False)

        patient.remarks = get_health_prediction(
            patient.glucose,
            patient.haemoglobin,
            patient.cholesterol
        )

        patient.save()

        return redirect('patient_list')

    return render(
        request,
        'patient/form.html',
        {'form': form}
    )
def patient_list(request):

    patients = Patient.objects.all()

    return render(
        request,
        'patient/list.html',
        {'patients': patients}
    )
def patient_update(request, pk):

    patient = get_object_or_404(
        Patient,
        id=pk
    )

    form = PatientForm(
        request.POST or None,
        instance=patient
    )

    if form.is_valid():

        patient = form.save(commit=False)

        patient.remarks = get_health_prediction(
            patient.glucose,
            patient.haemoglobin,
            patient.cholesterol
        )

        patient.save()

        return redirect('patient_list')

    return render(
        request,
        'patient/form.html',
        {'form': form}
    )
def patient_delete(request, pk):

    patient = get_object_or_404(
        Patient,
        id=pk
    )

    if request.method == "POST":

        patient.delete()

        return redirect('patient_list')

    return render(
        request,
        'patient/delete.html',
        {'patient': patient}
    )
