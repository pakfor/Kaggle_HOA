# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 18:00:14 2023

@author: NGPF

sampling_tools.py

"""
import random
import numpy as np

class SamplingTools():
    def sample_2d_patch(self, input_array, output_dim, output_number, preselected_pos=None, seed=None):
        """

        Parameters
        ----------
        input_array : numpy.ndarray
            An array that the patches are sampled from.
        output_dim : list
            A list that describes the dimension of output patch.
        output_number : int
            An integer that specifies how many patches should be returned.
        preselected_pos : list(list), optional
            A list of list of pre-selected positions
        seed : int, optional
            An integer that specifies the random seed. The default is None.

        Returns
        -------
        output_array : list(numpy.ndarray)
            A list of arrays of sampled patches.
        selection: list(list)
            A list of list of selected (sampled) positions

        """
        # If preselected_pos provided, match it with output_number
        if preselected_pos is not None:
            if not len(preselected_pos) == output_number:
                raise IndexError("The number of pre-selected positions does not match with number of output")

        all_sampled_patches = []
        all_selected_positions = []
        for i in range(0, output_number):
            if preselected_pos is not None:
                rand_1 = preselected_pos[i][0]
                rand_2 = preselected_pos[i][1]
            else:
                rand_1 = random.randint(0, input_array.shape[0] - output_dim[0])
                rand_2 = random.randint(0, input_array.shape[1] - output_dim[1])
            patch_temp = input_array[rand_1:rand_1 + output_dim[0],
                                     rand_2:rand_2 + output_dim[1],]
            all_sampled_patches.append(patch_temp)
            all_selected_positions.append([rand_1, rand_2])
        output_array = all_sampled_patches
        return output_array, all_selected_positions

    def sample_3d_patch(self, input_array, output_dim, output_number, preselected_pos=None, seed=None):
        """

        Parameters
        ----------
        input_array : numpy.ndarray
            An array that the patches are sampled from.
        output_dim : list
            A list that describes the dimension of output patch.
        output_number : int
            An integer that specifies how many patches should be returned.
        preselected_pos : list(list), optional
            A list of list of pre-selected positions
        seed : int, optional
            An integer that specifies the random seed. The default is None.

        Returns
        -------
        output_array : list(numpy.ndarray)
            A list of arrays of sampled patches.
        selection: list(list)
            A list of list of selected (sampled) positions

        """
        # If preselected_pos provided, match it with output_number
        if preselected_pos is not None:
            if not len(preselected_pos) == output_number:
                raise IndexError("The number of pre-selected positions does not match with number of output")

        all_sampled_patches = []
        all_selected_positions = []
        for i in range(0, output_number):
            if preselected_pos is not None:
                rand_1 = preselected_pos[i][0]
                rand_2 = preselected_pos[i][1]
                rand_3 = preselected_pos[i][2]
            else:
                rand_1 = random.randint(0, input_array.shape[0] - output_dim[0])
                rand_2 = random.randint(0, input_array.shape[1] - output_dim[1])
                rand_3 = random.randint(0, input_array.shape[2] - output_dim[2])
            patch_temp = input_array[rand_1:rand_1 + output_dim[0],
                                     rand_2:rand_2 + output_dim[1],
                                     rand_3:rand_3 + output_dim[2],]
            all_sampled_patches.append(patch_temp)
            all_selected_positions.append([rand_1, rand_2, rand_3])
        output_array = all_sampled_patches
        return output_array, all_selected_positions
